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
from modules.blockchain.serverchain import Blockchain
from bson.objectid import ObjectId
app = Flask(__name__)
CORS(app)

#Initializing credentials
keyids_json_path = r'modules/credentials/keyids.json'
service_account_json_path = r'modules/credentials/google_credentials.json'
default_data_json_path = r'modules/client/client_secrets/dummyJson.json'
MongoDB_CredentialsName = 'logincredentials'
GSheetStorageType = 'AdminPasswordChange'
globalSheetName = 'client_details'
mainCollection = "userdetails"
def configureKeys(path):
    with open(path) as f:
        data = json.load(f)
    return data
keyIDs = configureKeys(keyids_json_path)
defaultData = configureKeys(default_data_json_path)
#Variables
MongoDB_DatabaseName = 'mywatertech'
MongoDB_ClientDatabaseName = 'logincredentials'
MongoDB_UserDatabaseName = 'userdetails'
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

#BlockChainConnection


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
        details = {"Device_ID":str(resnew["_id"]),"Registerar_Email": resnew["Registerar_Email"],"Password":storage}
        response = adminDataBase.LoginDetailsUpdate(details,True,
                    MongoDB_CredentialsName,GSheetStorageType,globalSheetName,defaultData)
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
def fetchLoginData():
    datapacket = request.get_json()
    result = validator.LoginValidate(datapacket)
    if result["Is_Valid"]:
        block_response = adminDataBase.MongoDBBlockchain(result,MongoDB_ClientDatabaseName)
        industry_response,self_details = adminDataBase.MongoDBPrettyTableFetch(block_response["email"])
        #print(block_response)
        block_response["industry_response"] = industry_response
        block_response["self_details"] = self_details
        print(block_response)
        return jsonify(block_response)
    else:
        return(result)
    return result


# @app.route('/device-fetch', methods=['POST'])
# def FetchFromRaspberryPi():
#     datapacket = request.get_json()
#     res = validator.DeviceLoginValidate(datapacket)
#     if res["Is_Valid"]:
#         pass
#     return res

@app.route('/blockchain-device', methods=['POST'])
def FetchChain():
    datapacket = request.get_json()
    res = validator.DeviceLoginValidate(datapacket)
    if res["Is_Valid"]:
        Blockchain_Data = adminDataBase.MongoDBBlockchain(res,MongoDB_ClientDatabaseName)
        del(Blockchain_Data["_id"])
        del(Blockchain_Data["Password"])
        return jsonify(Blockchain_Data)
    return res

@app.route('/mine-block', methods=['POST'])
def MineBlock():
    datapacket = request.get_json()
    print("Request for change recieved")
    res = validator.DeviceLoginValidate(datapacket)
    if datapacket["Is_Valid"]:
        print("Data packet validated")
        updateMessage = adminDataBase.MongoDBBlockchainUpdate(datapacket,MongoDB_ClientDatabaseName)
    return(res)

@app.route('/fetch-client-details', methods=['POST'])
def FetchAll():
    datapacket = request.get_json()
    print(datapacket)
    res = validator.DeviceLoginValidate(datapacket)
    if res["Is_Valid"]:
        industryPacket = adminDataBase.MongoDBBlockchainAll(MongoDB_UserDatabaseName,datapacket["R_ID"],1)
        result = {"Industry":industryPacket}
        industryPacket = adminDataBase.MongoDBBlockchainAll(MongoDB_UserDatabaseName,datapacket["R_ID"],0)
        result["Self"] = industryPacket

    else:
        industryPacket={"Empty":"Empty Packet, Invalid Credentials."}
    return(jsonify(result))

@app.route('/make-a-transaction', methods=['POST'])
def Make_A_Transaction():
    datapacket = request.get_json()
    res = validator.LoginValidate(datapacket)
    senderEmail = datapacket["email"]
    if res["Is_Valid"]:
        senderID = adminDataBase.returnRegister_ID_FromEmail(senderEmail)
        senderID = senderID["_id"]
        recieverID = datapacket["_id"]
        print(senderID,recieverID)
        senderObject = Blockchain("_id",ObjectId(senderID),db,MongoDB_UserDatabaseName)
        recieveObject = Blockchain("_id",ObjectId(recieverID),db,MongoDB_UserDatabaseName)
        res = adminDataBase.Transaction_Chain(senderID,recieverID,int(datapacket["Credits"]))
        success_flag = res["Status"]
        print("Worked till here.")
        if success_flag:
            waterdetails = res["Transaction_chain"]
            print(waterdetails)
            senderObject.mine_block(waterdetails)
            #print(senderObject.chain)
            recieveObject.mine_block(waterdetails)
            #print(recieveObject.chain)
            print("Here as well")
            if senderObject.is_chain_valid() and recieveObject.is_chain_valid():
                adminDataBase.requestUpdate("_id",ObjectId(senderID),
                {"Transaction_So_Far":senderObject.chain})
                adminDataBase.requestUpdate("_id",ObjectId(recieverID),
                {"Transaction_So_Far":recieveObject.chain})
                print("Success!!!!!")
                return(jsonify({"Yes":"Transaction Successful!"}))

            else:
                return("Blockchain Disruption: Killing the process... Transaction Failed. Chain Invalid. Something is really very wrong.")
            # also check for chain validity before and after mining the block
        else:
            return(f"Transaction failed because of {res['Message']} Kindly retry.")

#Update Admin Sheet from Database

if __name__=="__main__":
    app.run(debug=True)
