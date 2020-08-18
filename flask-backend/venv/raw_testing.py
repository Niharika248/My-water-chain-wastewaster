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
livepeer = LivePeer(apiKey,LivePeerjsonBody,apiKeypath)
#adminDataBase.createDevices()
#print(adminDataBase.MongoDBPrettyTableFetch("sahil@gmail.com"))
#results = adminDataBase.FindDuplicates()
#Steps to Involve Blockchain-Verification
# print("Running")
# senderID = "5f298fd85d4eb1df1045fe60"
# mydata = adminDataBase.experimentationFunction(senderID)
# senderID = "5f298f7c56b378e6ff3c7fe4"
# recieverID = "5f298f7d56b378e6ff3c7fe5"
# blockchain = Blockchain("_id",ObjectId(senderID),db,MongoDB_DatabaseName)
# recieveObject = Blockchain("_id",ObjectId(recieverID),db,MongoDB_DatabaseName)
# res = adminDataBase.Transaction_Chain(senderID,recieverID,3)
# success_flag = res["Status"]
# waterdetails = res["Transaction_chain"]

# success_flag = res["Status"]
# if success_flag:
#     waterdetails = res["Transaction_chain"]
#     senderObject.mine_block(waterdetails)
#     print(senderObject.chain)
#     recieveObject.mine_block(waterdetails)
#     print(recieveObject.chain)
#     if senderObject.is_chain_valid() and recieveObject.is_chain_valid():
#         adminDataBase.requestUpdate("_id",ObjectId(senderID),
#         {"Transaction_So_Far":senderObject.chain})
#         adminDataBase.requestUpdate("_id",ObjectId(recieverID),
#         {"Transaction_So_Far":recieveObject.chain})
#         print("Blocks updated")
#     else:
#         print("Blockchain Disruption: Killing the process... Transaction Failed. Chain Invalid.")
#     # also check for chain validity before and after mining the block
#     print("Success")
# else:
#     print(f"Transaction failed because of {res['Message']}")




# senderID = adminDataBase.returnRegister_ID_FromEmail("shivam@gmail.com")
# senderID = "5f297e0f9f97b039dc8f6eb6"
# recieverID = "5f297e119f97b039dc8f6eb7"
#
# senderObject = Blockchain("_id",ObjectId(senderID),db,MongoDB_DatabaseName)
# recieveObject = Blockchain("_id",ObjectId(recieverID),db,MongoDB_DatabaseName)
#
# res = adminDataBase.Transaction_Chain(senderID,recieverID,2)
# success_flag = res["Status"]
# if success_flag:
#     waterdetails = res["Transaction_chain"]
#     senderObject.mine_block(waterdetails)
#     #print(senderObject.chain)
#     recieveObject.mine_block(waterdetails)
#     #print(recieveObject.chain)
#     if senderObject.is_chain_valid() and recieveObject.is_chain_valid():
#         adminDataBase.requestUpdate("_id",ObjectId(senderID),
#         {"Transaction_So_Far":senderObject.chain})
#         adminDataBase.requestUpdate("_id",ObjectId(recieverID),
#         {"Transaction_So_Far":recieveObject.chain})
#         return("Transaction Successful!")
#
#     else:
#         return("Blockchain Disruption: Killing the process... Transaction Failed. Chain Invalid. Something is really very wrong.")
#     # also check for chain validity before and after mining the block
# else:
#     return(f"Transaction failed because of {res['Message']} Kindly retry.")




#adminDataBase.createDevices()

#response = Blockchain("_id",ObjectId("5f27d280b700d27fd530a1f3"),db,mainCollection)


# val = adminDataBase.UpdateMongoByGSheet(sheet3,'PasswordChange','Password',
#                                         'Updated','PasswordChange','Credential_ID',
#                                         'logincredentials')


##emailcheck = validator.DuplicateEmailCheck('shifvam@gmail.com','logincredentials')
##print(emailcheck)


#id = 'a9eb3a5a-0e83-491b-bd59-8a0755018506'
# Live Peer Testing
#currentPlaybackurl = 'https://livepeer.com/api/ingest'
#res = livepeer.ReturnFetchUserUrl()
#print(res)
#livepeer.DisplayStreamingDetails()
#livepeer.FetchUserUrl('fb7aclz5no2kp2wg','4c8581f7-7714-4454-9ce9-d626f56db124')
#streamIds = livepeer.FetchAllStreamIds()
#livepeer.DisplayStreamingDetails()
#print(streamIds)
#print(f"response = {res}")
