import React,{useState} from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import RegistrationControl from '../constants/RegistrationFormControlOptions';
export default function RegisterScreen()
{
  const [credentials,setcredentials] = useState({
    Device_ID:"",
    Registerar_UserName:"",
    Registerar_Email:"",
    Organisation_Name:"",
    Organisation_Email:"",
    Password:"",
    Reenter_Password:""
  });

  function MapFields(props)
  {
    return<Form.Group key={props.id} autocomplete="off" controlId={props.formcontrolIdType}>
    <Form.Label>{props.fieldLabel}</Form.Label>
    <Form.Control type={props.fieldType} placeholder={props.fieldPlaceHolder}
    value={credentials[props.fieldDetails]} onChange={e=>{
      setcredentials({...credentials, [props.fieldDetails]: e.target.value});
      // ErrorChecker();
      }}
    />
    {  //<Form.Text className="text-muted">
      //{credentialMessage[props.fieldDetails]}
      //</Form.Text>
    }
  </Form.Group>;
  }

  return(
    <Form className="FormAligner">
    {RegistrationControl.map(MapFields)}
    <Button onClick={async(e)=>{
      e.preventDefault();
      const JSONString = credentials;
      const response = await fetch('http://localhost:5000/register',{
        method: 'POST',
        headers:{
          'Content-Type':'application/json'
        },
        body:JSON.stringify(JSONString)
      }).then(response=>response.json()).then((jsonData)=>{
        alert(jsonData["Error_Message"]);
      });
    }}>Submit</Button>
    </Form>
  );
}