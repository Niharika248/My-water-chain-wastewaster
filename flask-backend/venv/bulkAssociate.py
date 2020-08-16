#Bulk Associate

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
from modules.livepeer.LivePeer import LivePeer
from modules.blockchain.serverchain import Blockchain
from bson.objectid import ObjectId


#Initializing credentials

keyids_json_path = r'modules/credentials/keyids.json'
service_account_json_path = r'modules/credentials/google_credentials.json'
default_data_json_path = r'modules/client/client_secrets/dummyJson.json'
MongoDB_CredentialsName = 'logincredentials'
GSheetStorageType = 'AdminPasswordChange'
jsonBodypath = r'modules/livepeer/LivePeerAssets/credentials/test.json'
apiKeypath = r'modules/livepeer/LivePeerAssets/credentials/API_Key.json'

def configureKeys(path):
    with open(path) as f:
        data = json.load(f)
    return data
keyIDs = configureKeys(keyids_json_path)
defaultData = configureKeys(default_data_json_path)
#Variables
MongoDB_DatabaseName = 'mywatertech'
MongoDB_UserDatabaseName = 'userdetails'
gSheetKey = keyIDs["gSheetKey"]
mongoURI = keyIDs["mongoClientURI"]
mainCollection = "userdetails"

#gSheets
gc = gspread.service_account(filename = service_account_json_path)
sh = gc.open_by_key(gSheetKey)


client = pymongo.MongoClient(mongoURI)
db = client[MongoDB_DatabaseName]
#collection = db[MongoDB_CollectionName]

#LivePeer
LivePeerjsonBody = configureKeys(jsonBodypath)
apiKey = configureKeys(apiKeypath)

#Random Variables

sheet1 = 'client_details'
sheet3 = 'AdminPasswordChange'
#Giving Admin Access [to manipulate data]
adminDataBase = AdminDataBase(sh,db)
validator = Validator(sh,db)
print("Tried")
adminDataBase.createDevices()
