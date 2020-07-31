//0=> Check for Blanks 1=> Check for 12 character String
const RegistrationControl = [
    {
        id:0,
        formcontrolIdType:"formBasicText-0",
        fieldLabel:"Registration-ID",
        fieldType:"text",
        fieldPlaceHolder:"Enter the 12 digit Registration ID",
        fieldDetails:"Device_ID",
    },
    {
        id:1,
        formcontrolIdType:"formBasicText-1",
        fieldLabel:"Registerar Username",
        fieldType:"text",
        fieldPlaceHolder:"Enter your Username.",
        fieldDetails:"Registerar_UserName",
    },
    {
        id:2,
        formcontrolIdType:"formBasicEmail-0",
        fieldLabel:"Registerar Email ID",
        fieldType:"email",
        fieldPlaceHolder:"Enter your Email-ID.",
        fieldDetails:"Registerar_Email",
    },
    {
        id:3,
        formcontrolIdType:"formBasicText-2",
        fieldLabel:"Organisation Name",
        fieldType:"text",
        fieldPlaceHolder:"Enter your Water Provider.",
        fieldDetails:"Organisation_Name",
    },
    {
        id:4,
        formcontrolIdType:"formBasicEmail-1",
        fieldLabel:"Organisation Email",
        fieldType:"email",
        fieldPlaceHolder:"Enter Water Provider ID.",
        fieldDetails:"Organisation_Email",
    },
    {
        id:5,
        formcontrolIdType:"formBasicPassword-0",
        fieldLabel:"Password",
        fieldType:"password",
        fieldPlaceHolder:"Enter Password.",
        fieldDetails:"Password",
    },
    {
        id:6,
        formcontrolIdType:"formBasicPassword-1",
        fieldLabel:"Re-enter Password",
        fieldType:"password",
        fieldPlaceHolder:"Re-enter Password.",
        fieldDetails:"Reenter_Password",
    },

];
export default RegistrationControl;