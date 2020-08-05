import React, { useState } from 'react';
import DummyDetails,{ TableHeaders,MyTableHeaders,MyTableDetails} from '../constants/dummyconstantfiles.js';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
function PrettyTable(props)
{
    const FetchedData = props.Data;
    const SelfData = props.selfData;

    const [details,setpurchaseDetails] = useState({
        _id:null,
        Credits:null
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
        <Form.Group className="Purchase-Reuester-Column" key={1} autocomplete="off" controlId="PurchaseEntry">
        <Form.Label>Industry-ID</Form.Label>
        <Form.Control type="text" placeholder="Enter Industry-ID"
        value={details._id} onChange={val=>{setpurchaseDetails({...details, ["_id"]: val.target.value});}}/>
      </Form.Group>
      <Form.Group className="Purchase-Reuester-Column" key={1} autocomplete="off" controlId="PurchaseCredit">
        <Form.Label>Water Drops</Form.Label>
        <Form.Control type="text" placeholder="Enter Water Drops"
        value={details.Credits} onChange={val=>{setpurchaseDetails({...details, ["Credits"]: val.target.value});}}/>
      </Form.Group>
      <Button className="Purchase-Requester-Column" onClick={async(e)=>{
        e.preventDefault();
        let pwd = prompt('Please enter your Password to confirm!');
        const JSONString = {
            email:props.Email,
            _id:details._id,
            Credits:details.Credits,
            password:pwd
        }
        const response = await fetch('http://localhost:5000/make-a-transaction',{
          method: 'POST',
          headers:{
            'Content-Type':'application/json'
          },
          body:JSON.stringify(JSONString)
        });
        console.log("Hello "+response.json());
      }}>Purchase</Button>
      </div>
        </div>
        </div>
    );
}

export default PrettyTable;