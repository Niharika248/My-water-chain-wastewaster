#Raw testing

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


client = pymongo.MongoClient(mongoURI)
db = client[MongoDB_DatabaseName]
#collection = db[MongoDB_CollectionName]

#Random Variables

sheet1 = 'client_details'
sheet3 = 'AdminPasswordChange'
#Giving Admin Access [to manipulate data]
adminDataBase = AdminDataBase(sh,db)
validator = Validator(sh,db)

adminDataBase.createDevices()

# val = adminDataBase.UpdateMongoByGSheet(sheet3,'PasswordChange','Password',
#                                         'Updated','PasswordChange','Credential_ID',
#                                         'logincredentials')


##emailcheck = validator.DuplicateEmailCheck('shifvam@gmail.com','logincredentials')
##print(emailcheck)
