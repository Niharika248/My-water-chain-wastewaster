import pymongo
import datetime
from bson.objectid import ObjectId
import json
from modules.encoding.password_encoder import EnforceSecurity
#Variables
##keyids_json_path = r'modules/credentials/keyids.json'
##service_account_json_path = r'modules/credentials/google_credentials.json'
MongoDB_DatabaseName = 'mywatertech'
MongoDB_CollectionName = 'userdetails'
MongoDB_CredentialsName = 'logincredentials'
createDevice_MessageCode = 'TRUE'
update_MessageCode = 'Updated'
ActiveDeviceStatus = "Active"
ErrorMessages = {
    "Device_ID":"Invalid Device-ID, you must first get your device registered by administrator.",
    "Registerar_Email":"Invalid Registerar Email! Doesn't Exist.",
    "Registerar_UserName":"Invalid Registerar Username! Doesn't Exist",
    "Organisation_Name":"You have a typo in your Organisation's name. Kindly Recheck",
    "Organisation_Email":"Invalid Organisation Email! Kindly Contect your provider.",
    "Password":"Passwords don't Match.",
    "ActiveDevice":"There is an existing account with this device name.!",
    "DuplicateEmail":"Seems like the email is wrongly associated and already exists with another account. Kindly contact administrator!",
    "LoginEmailError":"Email doesn't Exist!",
    "LoginSuccess":"Login Successful!",
    "IncorrectPassword":"Incorrect Password! Please try again."
    }
SuccessMessage = "Registration Successful! you may login now."

class Validator:
    def __init__(self,sh,db):
        self.response = {
            "Device_ID":'',"Registerar_UserName":'',"Registerar_Email":'',
            "Organisation_Name":'',"Organisation_Email":'',"Password":'',
            "Reenter_Password":'',"Error_Message":"0","Is_Valid":False
            }
        self.loginresponse ={
            "Is_Valid":False,
            "Error_Message":""
            }
        self.ErrorMessage = ''
        self.sh = sh
        self.db = db
        self.collection = db[MongoDB_CollectionName]
    def DuplicateEmailCheck(self,email,collectionname):
        collection = self.db[collectionname]
        res = collection.find_one({"Registerar_Email": email})
        if(res==None):return(False)
        else:return(True)
    def LoginValidate(self,details,MongoDB_CredentialsName=MongoDB_CredentialsName):
        collection = self.db[MongoDB_CredentialsName]
        email = details["email"]
        password = details["password"]
        res = collection.find_one({"Registerar_Email": email})
        if res==None:
            self.loginresponse["Error_Message"] = ErrorMessages["LoginEmailError"]
        else:
            storage = res["Password"]
            validatePW = EnforceSecurity({"password":password,
                                                   "storage":storage})
            self.loginresponse["Is_Valid"] = validatePW.DecodePassword()
            if self.loginresponse["Is_Valid"]:
                self.loginresponse["Error_Message"] = ErrorMessages["LoginSuccess"]
            else:
                self.loginresponse["Error_Message"] = ErrorMessages["IncorrectPassword"]
        return(self.loginresponse)
    def DeviceLoginValidate(self,details,MongoDB_CredentialsName=MongoDB_CredentialsName):
        collection = self.db[MongoDB_CredentialsName]
        res = self.collection.find_one({"_id": ObjectId(details["Device_ID"])})
        if res==None:
            self.loginresponse["Error_Message"] = ErrorMessages["Device_ID"]
        else:
            self.loginresponse = self.LoginValidate(details,MongoDB_CredentialsName=MongoDB_CredentialsName)
            self.loginresponse["email"] = details["email"]
            self.loginresponse["password"] = details["password"]
        return(self.loginresponse)

    def ValidateData(self,ExternalData):
        device_id = ExternalData["Device_ID"]
        try:
            res = self.collection.find_one({"_id": ObjectId(device_id)})
            if ExternalData["Registerar_UserName"]!=res["Registerar_UserName"]:
                self.response["Error_Message"] = ErrorMessages["Registerar_UserName"]
            elif ExternalData["Registerar_Email"]!=res["Registerar_Email"]:
                self.response["Error_Message"] = ErrorMessages["Registerar_Email"]
            elif ExternalData["Organisation_Name"]!=res["Organisation_Name"]:
                self.response["Error_Message"] = ErrorMessages["Organisation_Name"]
            elif ExternalData["Organisation_Email"]!=res["Organisation_Email"]:
                self.response["Error_Message"] = ErrorMessages["Organisation_Email"]
            elif ExternalData["Password"]!=ExternalData["Reenter_Password"]:
                self.response["Error_Message"] = ErrorMessages["Password"]
            elif res["Device_Status"] == ActiveDeviceStatus:
                self.response["Error_Message"] = ErrorMessages["ActiveDevice"]
            elif self.DuplicateEmailCheck(ExternalData["Registerar_Email"],MongoDB_CredentialsName):
                self.response["Error_Message"]=ErrorMessages["DuplicateEmail"]
            else:
                self.collection.update_one({"_id": ObjectId(device_id)},{"$set":{"Device_Status":ActiveDeviceStatus}})
                self.response = res
                self.response["_id"] = str(res["_id"])
                self.response["Password"] = ExternalData["Password"]
                self.response["Is_Valid"] = True
                self.response["Error_Message"] = SuccessMessage

        except:
            self.response["Error_Message"] = ErrorMessages["Device_ID"]
        return(self.response)
