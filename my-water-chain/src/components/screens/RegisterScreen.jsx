import React,{useState} from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import RegistrationControl from '../constants/RegistrationFormControlOptions';
import Spinner from 'react-bootstrap/Spinner';
import Footer from "../junk/Footer";
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

  const [loading,setloading] = useState(false);

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

  return(<div>
    <Form className="FormAligner">
    {RegistrationControl.map(MapFields)}
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
      const response = await fetch('http://localhost:5000/register',{
        method: 'POST',
        headers:{
          'Content-Type':'application/json'
        },
        body:JSON.stringify(JSONString)
      }).then(response=>response.json()).then((jsonData)=>{
        setloading(false);
        alert(jsonData["Error_Message"]);
      });
    }}>Submit</Button></div>}
    <Footer />
    </Form>
    </div>
  );
}