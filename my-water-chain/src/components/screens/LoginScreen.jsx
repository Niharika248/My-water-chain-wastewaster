import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ErrorCodes from '../constants/ErrorCodes.jsx';
import LoginDetails from '../constants/LoginDetails.jsx';
import Auth from '../security/Auth.jsx';
export default function LoginScreen(props)
{
  const [credentials,setCredentials] = useState({
    email:"",
    password:""
  });
  const [credentialMessage,setcredentialMessage]=useState({
    email:"",
    password:""
  });
  function ErrorChecker()
  {
    let regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(regex.test(credentials["email"]))
      setcredentialMessage({...credentialMessage, ["email"]: ErrorCodes[0]});
 
    else
      setcredentialMessage({...credentialMessage, ["email"]: ErrorCodes[4]});

  }
  function LoginScreenRenderer(props)
  {
    return <Form.Group key={props.id} autocomplete="off" controlId={props.controlId}>
    <Form.Label>{props.Label}</Form.Label>
    <Form.Control type={props.type} placeholder={props.placeholder}
    value={credentials[props.type]} onChange={e=>{
      setCredentials({...credentials, [props.type]: e.target.value});
      ErrorChecker();
      }}
    />
    <Form.Text className="text-muted">
      {credentialMessage[props.type]}
      </Form.Text>
  </Form.Group>;
  }
  return(
    <Form className="FormAligner">
    {LoginDetails.map(LoginScreenRenderer)}
    <Button onClick={async(e)=>{
      e.preventDefault();
      const JSONString = credentials;
      const response = await fetch('http://localhost:5000/login',{
        method: 'POST',
        headers:{
          'Content-Type':'application/json'
        },
        body:JSON.stringify(JSONString)
      }).then(response=>response.json()).then(async(jsonData)=>{
        if(jsonData["Is_Valid"])
        {
          const BackendData = await fetch('http://localhost:5000/fetching',{
            method: 'POST',
            headers:{
              'Content-Type':'application/json'
            },
            body:JSON.stringify(JSONString)
          }).then(response=>response.json()).then((jsonBackend)=>{
            //properties-> jsonBackend
            Auth.login(jsonBackend);
            props.history.push("/login-props-test");
          });
          
        }
        else
        {
          alert("Invalid Credentials! Error Message: "+jsonData["Error_Message"]);
        }
      });
    }}>Submit</Button>
    </Form>
  );
}