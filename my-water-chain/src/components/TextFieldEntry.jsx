import React, { useState } from "react";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import ErrorCodes from './ErrorCodes.jsx';

export default function TextFieldEntry(props)
{

   const [fieldValue,setFieldValue] = useState('');
   const [ErrorMessage,setErrorMessage] = useState('');
   function checkForErrors(errorcode,stringValue)
   {
      fieldValue = setFieldValue(stringValue);
      if(!errorcode)
      {
         console.log("Debugging for error code: 0");
         if(fieldValue.length===0)
         setErrorMessage(ErrorCodes[0]);
         else
         setErrorMessage(ErrorCodes[1]);

      }
      
   }
   return(
  <Form.Group controlId={props.formcontrolIdType}>
    <Form.Label>{props.fieldLabel}</Form.Label>
    <Form.Control type={props.fieldType} autocomplete="off" placeholder={props.fieldPlaceHolder} value={fieldValue}
    onChange={e=>{checkForErrors(props.ErrorCheckType,e.target.value);}}/>
    <Form.Text className="text-muted" value={ErrorMessage}></Form.Text>
  </Form.Group>
  );
}