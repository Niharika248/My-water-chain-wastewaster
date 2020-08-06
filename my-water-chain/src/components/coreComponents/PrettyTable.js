import React, { useState } from 'react';
import { TableHeaders,MyTableHeaders} from '../constants/dummyconstantfiles.js';
import { useHistory } from "react-router-dom";
import Spinner from 'react-bootstrap/Spinner';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Auth from '../security/Auth.jsx';

function PrettyTable(props)
{
    let history = useHistory();
    const FetchedData = props.Data;
    const SelfData = props.selfData;
    const [PasswordPrompt,updatePasswordPrompt] = useState(false);
    const [loaded,loading] = useState(false);

    const [details,setpurchaseDetails] = useState({
        _id:null,
        Credits:null,
        Password:null,
    });

    return(
        <div>
        <h3 className="My-Table-Details-01">Industrial Performance</h3>
        <table className="Pretty-Table">
        {TableHeaders.map(header=>{
            return(<th className="Pretty-Table-Header">{header}</th>);
        })}
        {
            FetchedData.map(props=>{
                return(<tr className="Pretty-Table-Row">
                    <td className="Pretty-Table-Body">
                    {props.Registerar_UserName}
                    </td>
                    <td className="Pretty-Table-Body">
                    {props._id}
                    </td>
                    <td className="Pretty-Table-Body">
                    {props.Allowance}
                    </td>
                    <td className="Pretty-Table-Body">
                    {props.Credits}
                    </td>
                    </tr>);
            })
        }
        </table>
        <h3 className="My-Table-Details">My Details</h3>
        <table className="Pretty-Table">
        {
            MyTableHeaders.map(header=>{
                return(<th className="My-Pretty-Table-Header">{header}</th>);
            })
        }
        (<tr className="Pretty-Table-Row">
        {
            SelfData.map(detail=>{
                return(<td className="Pretty-Table-Body">
                {detail}
                </td>);
            })
        }
        </tr>
        </table>
        <div className="Purchase-Reuqester">
        <div>
        <Form.Group className="Purchase-Reuester-Column" key={1} autoComplete="off" controlId="PurchaseEntry">
        <Form.Label>Industry-ID</Form.Label>
        <Form.Control type="text" placeholder="Enter Industry-ID"
        value={details._id} onChange={val=>{setpurchaseDetails({...details, ["_id"]: val.target.value});}}/>
      </Form.Group>
      <Form.Group className="Purchase-Reuester-Column" key={2} autoComplete="off" controlId="PurchaseCredit">
        <Form.Label>Water Drops</Form.Label>
        <Form.Control type="text" placeholder="Enter Water Drops"
        value={details.Credits} onChange={val=>{setpurchaseDetails({...details, ["Credits"]: val.target.value});}}/>
      </Form.Group>
      {PasswordPrompt?<div>
        <div className="Purchase-Reuqester">
        <Form.Group className="Purchase-Reuester-Column" key={3} autoComplete="off" controlId="Password">
        <Form.Label>Password</Form.Label>
        <Form.Control type="password" placeholder="Confirm Password"
        value={details.Password} onChange={val=>{setpurchaseDetails({...details, ["Password"]: val.target.value});}}/>
      </Form.Group>
        </div>
        {loaded?<Button className="Purchase-Reuqester"
        variant="primary" disabled>
        <Spinner
          as="span"
          animation="border"
          size="sm"
          role="status"
          aria-hidden="true"
        />
        <span className="sr-only">Loading...</span>
      </Button>:<Button className="Purchase-Reuqester" onClick={async(e)=>{
        e.preventDefault();
        loading(true);
        const JSONString = {
            email:props.Email,
            _id:details._id,
            Credits:details.Credits,
            password:details.Password
        }
        const response = await fetch('http://localhost:5000/make-a-transaction',{
            method: 'POST',
            headers:{
              'Content-Type':'application/json'
             },
             body:JSON.stringify(JSONString)
         });

        const content = await response.json();
        loading(false);
        console.log(props);
        Auth.login(content);
        history.push("/login-props-test");
      }}>Purchase</Button>
    }
        </div>:<div className="Purchase-Reuqester">
        <Button className = "Purchase-Requester-Column" onClick={
            e=>{
                e.preventDefault();
                updatePasswordPrompt(true);
            }
        }>Procceed</Button>
        </div>}
      </div>
        </div>
        </div>
    );
}

export default PrettyTable;
