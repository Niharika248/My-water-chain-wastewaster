#Main Program
from flask import Flask,jsonify,request
import datetime
import gspread
import json
import pymongo
import pandas as pd
from flask_cors import CORS
from modules.databases.gSheet_MongoDB import AdminDataBase
from modules.databases.form_validator import Validator
from modules.encoding.password_encoder import EnforceSecurity
app = Flask(__name__)
CORS(app)

#Initializing credentials
keyids_json_path = r'modules/credentials/keyids.json'
service_account_json_path = r'modules/credentials/google_credentials.json'
MongoDB_CredentialsName = 'logincredentials'
GSheetStorageType = 'AdminPasswordChange'
globalSheetName = 'client_details'
def configureKeys():
    with open(keyids_json_path) as f:
        data = json.load(f)
    return data
keyIDs = configureKeys()

#Variables
MongoDB_DatabaseName = 'mywatertech'
gSheetKey = keyIDs["gSheetKey"]
mongoURI = keyIDs["mongoClientURI"]

#gSheets
gc = gspread.service_account(filename = service_account_json_path)
sh = gc.open_by_key(gSheetKey)
#worksheet = sh.sheet1
#bulksheet =  sh.worksheet(bulk_associate_sheet_name)

#MongoDB
client = pymongo.MongoClient(mongoURI)
db = client[MongoDB_DatabaseName]
#collection = db[MongoDB_CollectionName]

#Giving Admin Access [to manipulate data]
adminDataBase = AdminDataBase(sh,db)
validator = Validator(sh,db)
print("Successfully configured all the admin Databases and GSheets.")
@app.route('/register', methods=['POST'])
def postRegistrationData():
    datapacket = request.get_json()
    #print(datapacket)
    resnew = validator.ValidateData(datapacket)
    if resnew["Is_Valid"]:
        security = EnforceSecurity({"password":resnew["Password"],"storage":''})
        storage = security.EncodePassword()
        print(resnew)
        details = {"Device_ID":str(resnew["_id"]),"Registerar_Email": resnew["Registerar_Email"],"Password":storage}
        response = adminDataBase.LoginDetailsUpdate(details,True,
                                                    MongoDB_CredentialsName,GSheetStorageType,globalSheetName) 
    #print(datapacket["Device_ID"])
    return resnew

@app.route('/login', methods=['POST'])
def postLoginData():
    datapacket = request.get_json()
    result = validator.LoginValidate(datapacket)
    if result["Is_Valid"]:
        print("Login Success")
    else:
        print("Login Failure")
    return result

@app.route('/fetching', methods=['POST'])
def testLoginData():
    datapacket = request.get_json()
    email = datapacket["email"]
    #print(f"Data recieved: @ {datapacket}")
    return datapacket


if __name__=="__main__":
    app.run(debug=True)


#Feature Addition:
#for emails also ensure that each registration has unique emails
