import React, { useState } from 'react';
import DummyDetails,{ TableHeaders,MyTableHeaders,MyTableDetails} from '../constants/dummyconstantfiles.js';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
function PrettyTable(props)
{
    const [yourCredits,setyourCredits] = useState(MyTableDetails[0]);
    const [counter,setCounter] = useState(0);
    const [purchaseDetails,setpurchaseDetails] = useState({
        id:'',
        credits:null,
    });

    return(
        <div>
        <table className="Pretty-Table">
        {TableHeaders.map(header=>{
            return(<th className="Pretty-Table-Header">{header}</th>);
        })}
        {
            DummyDetails.map(props=>{
                return(<tr className="Pretty-Table-Row">
                    <td className="Pretty-Table-Body">
                    {props.IndustryName}
                    </td>
                    <td className="Pretty-Table-Body">
                    {props.IndustryID}
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
        <table className="Pretty-Table">
        {
            MyTableHeaders.map(header=>{
                return(<th className="My-Pretty-Table-Header">{header}</th>);
            })
        }
        (<tr className="Pretty-Table-Row">
        {
            MyTableDetails.map(detail=>{
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
        value={purchaseDetails.id} onChange={val=>{setpurchaseDetails({...purchaseDetails, ["id"]: val.target.value});}}/>
      </Form.Group>
      <Form.Group className="Purchase-Reuester-Column" key={1} autocomplete="off" controlId="PurchaseCredit">
        <Form.Label>Water Drops</Form.Label>
        <Form.Control type="text" placeholder="Enter Water Drops"
        value={purchaseDetails.credits} onChange={val=>{setpurchaseDetails({...purchaseDetails, ["credits"]: val.target.value});}}/>
      </Form.Group>
      <Button className="Purchase-Requester-Column">Purchase</Button>
      </div>
        </div>
        </div>
    );
}

export default PrettyTable;