import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ErrorCodes from '../constants/ErrorCodes.jsx';
import LoginDetails from '../constants/LoginDetails.jsx';
import Spinner from 'react-bootstrap/Spinner';
import Auth from '../security/Auth.jsx';
import Footer from '../junk/Footer';
import {ipaddress} from "../constants/dummyconstantfiles";

export default function LoginScreen(props)
{
  const [credentials,setCredentials] = useState({
    email:"",
    password:""
  });
  const [loading,setloading] =useState(false);
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
    return <Form.Group key={props.id} autoComplete="off" controlId={props.controlId}>
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
    <div>
    <Form className="FormAligner">
    {LoginDetails.map(LoginScreenRenderer)}
    {loading?<div className="UI-Aligner">

      <Button className="UI-Button-Click" variant="primary" disabled>
    <Spinner
      as="span"
      animation="border"
      size="sm"
      role="status"
      aria-hidden="true"
    />
    <span className="sr-only">Loading...</span>
    </Button> 
      </div>:<div className="UI-Aligner"><Button className="UI-Button-Click" onClick={async(e)=>{
      e.preventDefault();
      setloading(true);
      const JSONString = credentials;
      const response = await fetch(`${ipaddress}login`,{
        method: 'POST',
        headers:{
          'Content-Type':'application/json'
        },
        body:JSON.stringify(JSONString)
      }).then(response=>response.json()).then(async(jsonData)=>{
        if(jsonData["Is_Valid"])
        {
          const BackendData = await fetch(`${ipaddress}fetching`,{
            method: 'POST',
            headers:{
              'Content-Type':'application/json'
            },
            body:JSON.stringify(JSONString)
          }).then(response=>response.json()).then((jsonBackend)=>{
            //properties-> jsonBackend
            setloading(false);
            Auth.login(jsonBackend);
            props.history.push("/login-props-test");
          });
          
        }
        else
        {
          setloading(false);
          alert("Invalid Credentials! Error Message: "+jsonData["Error_Message"]);
        }
      });
    }}>Login</Button></div>}
    </Form>
    <Footer />
    </div>
  );
}