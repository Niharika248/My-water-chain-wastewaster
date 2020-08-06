#Importing Useful Libraries
import gspread
import pandas as pd
import pymongo
import datetime
from bson.objectid import ObjectId
import json
from modules.encoding.password_encoder import EnforceSecurity
#Useful Config Variables

DeviceStatusHeading = 'Device_Status' #To locate the header for device status (by index)
Device_ID = 'Device_ID' #To locate index of Device ID and do active changes based on database
bulk_associate_sheet_name = 'bulk_associate' #Second spreadsheet name
MongoDB_DatabaseName = 'mywatertech'
MongoDB_CollectionName = 'userdetails'
MongoDB_LoginCollectionName = 'logincredentials'
createDevice_MessageCode = 'TRUE'
update_MessageCode = 'Updated'
AdminPasswordChangeRequest = 'AdminPasswordChange'
AdminPasswordChangeHeader = 'PasswordChange'
MongoDBPasswordField = 'Password'
BlockChainConnection = 'blockchain'
PasswordChangeStaticName = update_MessageCode
perCreditAllowance = 25
cutoffFactor = 0.1
defData = [{"From":"","To":"","Credits":"","TimeStamp":""}]




#different ways to fetch data:
#res = worksheet.get_all_records()
#res = worksheet.get_all_values()
#res = worksheet.col_values()
#res = worksheet.get('A2:C2')

class AdminDataBase:
    def __init__(self,sheet,client):
        self.operation=0 #Operation 0 refers to additional database
        self.Device_Status_Index = 6 #Initial Device Status
        self.NumberOfDevices = 0 #Number of Devices to create
        self.EmailAssociation = False #Getting
        self.sh = sheet
        self.db = client
        self.collection = self.db[MongoDB_CollectionName]
        self.loginCollection = self.db[MongoDB_LoginCollectionName]
        self.worksheet = self.sh.sheet1
        self.bulksheet = self.sh.worksheet(bulk_associate_sheet_name)

    def getMongoDBCollection(self,collectionName):
        return(self.db[collectionName])

    def GetTimeStamp(self):
        timestamp = str(datetime.datetime.now()).split(":")
        try:return(timestamp[0]+":"+timestamp[1]+ " hrs")
        except: return(str(datetime.datetime.now()))

    def GetIndexByHeader(self,HeaderString,sheetType):
        Headers = sheetType.row_values(1)
        return(Headers.index(HeaderString))

    def create_block(self, proof, previous_hash,chainlength,defaultData):
        block = {'index': chainlength + 1,
                 'timestamp': self.GetTimeStamp(),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'water_data':defaultData
                 }
        return block
    def isDuplicate(self,email):
        query = {}
        fields = {"Registerar_Email":1}
        results = self.collection.find(query,fields)
        emails = [r["Registerar_Email"] for r in results]
        if email in emails:
            return True
        else:
            return False

    def createDevices(self):
        newEntries = self.bulksheet.get_all_records()[0:]
        StatusIndex = self.GetIndexByHeader("Status",self.bulksheet)
        cellEntry = 0
        for entry in newEntries:
            if entry["Status"]==createDevice_MessageCode:
                pass
            else:
                if self.isDuplicate(entry["Registerar_Email"]):
                    print(f"Process Aborted for Email-ID: {entry['Registerar_Email']} Duplicate email associate attempt!")
                    self.bulksheet.update_cell(cellEntry+2,StatusIndex+1,"Process Failed Due to Duplicacy")
                else:
                    timestamp = self.GetTimeStamp()
                    _id = self.collection.insert({"Registerar_UserName":entry["Registerar_UserName"],
                                             "Registerar_Email":entry["Registerar_Email"],
                                             "Organisation_Name":entry["Organisation_Name"],
                                             "Organisation_Email":entry["Organisation_Email"],
                                             "Allowance":entry["Allowance"],
                                             "Credits":entry["Credits"],
                                             "Expiry_Date": self.getTodayDate(),
                                             #"Block_Chain":[self.create_block(1,'0',0,defaultData)],
                                             "Transaction_So_Far":[self.create_block(1,'0',0,defData)],
                                             "Device_Status":"Inactive",
                                             "TimeStamp":timestamp})
                    data = [f"{str(_id)}",entry["Registerar_UserName"],
                            entry["Registerar_Email"],
                            entry["Organisation_Name"],entry["Organisation_Email"],
                            entry["Allowance"],"Inactive","Updated",timestamp]
                    #print(data)
                    #worksheet.insert_row(data,rownumber=3)
                    self.worksheet.append_row(data)
                    self.bulksheet.update_cell(cellEntry+2,StatusIndex+1,"TRUE")

            cellEntry+=1

    def UpdateDataBaseFromGSheets(self):
        newEntries = self.worksheet.get_all_records()[0:]
        StatusIndex = self.GetIndexByHeader("Update_Status",self.worksheet)
        rownum=2
        for entry in newEntries:
            if entry["Update_Status"]==update_MessageCode:pass
            else:
                timestamp = self.GetTimeStamp()
                print(entry["Organisation_Name"])
                print(entry["Device_ID"])
                newdata = {"Registerar_UserName":entry["Registerar_UserName"],
                                     "Registerar_Email":entry["Registerar_Email"],
                                     "Organisation_Name":entry["Organisation_Name"],
                                     "Organisation_Email":entry["Organisation_Email"],
                                     "Allowance":entry["Allowance"],
                                     "Credits":entry["Credits"],
                                     "Device_Status":"Inactive",
                                     "TimeStamp":timestamp}
                self.collection.update({"_id":ObjectId(entry["Device_ID"])},{"$set":newdata})
                self.worksheet.update_cell(rownum,StatusIndex+2,timestamp)
                self.worksheet.update_cell(rownum,StatusIndex+1,"Updated")
            rownum+=1

    def getTodayDate(self):
        timestamp = datetime.datetime.now().timestamp()
        timestamp = timestamp+(60*60*24*30)
        newDate = datetime.datetime.fromtimestamp(timestamp)
        return(datetime.datetime.strptime(str(newDate).split(" ")[0], "%Y-%m-%d").strftime("%d-%B-%Y"))

    def LoginDetailsUpdate(self,details,isAdd,collectionType,sheetType,globalSheetName,defaultData):
        if isAdd:
            collection = self.db[collectionType]
            details["TimeStamp"] = self.GetTimeStamp()
            details["Block_Chain"] = [self.create_block(1,'0',0,defaultData)]
            _id = collection.insert(details)
            data = [str(_id),details["Device_ID"],details["Registerar_Email"],
            details["TimeStamp"],PasswordChangeStaticName]
            activeSheet = self.sh.worksheet(sheetType)
            activeSheet.append_row(data)
            self.UpdateGSheetFromDbase(details["Device_ID"],globalSheetName)
            return("Success")
        else:
            return("NA")
    def getSheet(self,SheetName):
        return (self.sh.worksheet(SheetName),self.sh.worksheet(SheetName).row_values(1))

    def UpdateGSheetFromDbase(self,searchID,SheetName):
        sheet,Headers = self.getSheet(SheetName)
        index = Headers.index(Device_ID)
        rowVal = sheet.find(searchID,in_column = index+1).row #.col for column
        index = Headers.index(DeviceStatusHeading)
        #val = sheet.cell(rowVal,index+1).value
        sheet.update_cell(rowVal,index+1,"Active")

    def UpdateMongoByGSheet(self,sheetName,SheetHeader,MongoDBField,
                            StaticName,gSheetHeaderReflecter,IdentityofDB,
                            MongoDBCollectionName):
        sheet,Headers = self.getSheet(sheetName)
        updatorList = []
        HeaderIndex = Headers.index(SheetHeader)+1
        Entries = sheet.get_all_records()[0:]
        entryIndex = 2
        for Entry in Entries:
            if Entry[gSheetHeaderReflecter]!=StaticName:
                passwordValue = Entry[gSheetHeaderReflecter]
                IdentificationID = Entry[IdentityofDB]
                enforcePassword = EnforceSecurity({"password":passwordValue,
                                                   "storage":""})
                storage = enforcePassword.EncodePassword()
                collection = self.getMongoDBCollection(MongoDBCollectionName)
                newdata = collection.find_one({"Device_ID":IdentificationID})
                newdata['Password'] = storage
                print(newdata)
                collection.update({"Device_ID":IdentificationID},{"$set":newdata})
                sheet.update_cell(entryIndex,HeaderIndex,StaticName)
            entryIndex+=1


    def MongoDBBlockchain(self,details,collectionType):
        collection = self.getMongoDBCollection(collectionType)
        query = {"Registerar_Email":details["email"]}
        field = {"Block_Chain":1}
        res = collection.find_one(query,field)
        res["Is_Valid"] = details["Is_Valid"]
        res["Error_Message"] = details["Error_Message"]
        res["email"] = details["email"]
        del(res["_id"])
        return res


    # def MongoDBBlockchainUpdate(self,details,collectionType):
    #     collection = self.getMongoDBCollection(collectionType)
    #     myquery = {"_id": ObjectId(details["Device_ID"])}
    #     newvalues = { "$set": {"Block_Chain":details["Block_Chain"]} }
    #     print(type(details["Block_Chain"]))
    #     result = collection.update_one(myquery,newvalues)
    #     print(result.raw_result)
    #     print(result.acknowledged)
    #     return "OK"

    def MongoDBBlockchainAll(self,collectionType,deviceID,decision):
        collection = self.getMongoDBCollection(collectionType)
        if decision:
            query={'_id': {"$ne" : ObjectId(deviceID)}}
        else:
            query = {'_id':ObjectId(deviceID)}
        fields = {"Registerar_UserName":1,"_id":1,"Allowance":1,"Credits":1,"Expiry_Date":1}
        res = list(collection.find(query,fields))
        for object in res:
            ids = str(object["_id"])
            del(object["_id"])
            object["_id"] = ids
        return(res)

    def MongoDBPrettyTableFetch(self,emailID):
        query = {"Registerar_Email":{"$ne" : emailID},"Device_Status":"Active"}
        fields = {"Registerar_UserName":1,"_id":1,"Allowance":1,"Credits":1}
        res = list(self.collection.find(query,fields))
        #res = [str(a["_id"]) for a in res]
        for r in res:
            r["_id"]=str(r["_id"])
        query["Registerar_Email"] = emailID
        fields ={"Credits":1,"Allowance":1,"Expiry_Date":1}
        response = self.collection.find_one(query)
        del(response["_id"])
        responselist = [response["Credits"],response["Allowance"],response["Expiry_Date"]]
        return(res,responselist)

    def isResponseEmpty(self,response):
        if response is None:
            return(True)
        elif len(response)==0:
            return(True)
        else:
            return False
    def returnServerChain(self,client_ID):
        from_query = {"_id":ObjectId(client_ID)}
        field = {"Transaction_So_Far":1}
        collection_chain = self.collection.find_one(from_query,field)
        return(collection_chain)

    def returnRegister_ID_FromEmail(self,emailID):
        from_query = {"Registerar_Email":emailID}
        field = {"_id":1}
        idc = self.collection.find_one(from_query,field)
        idc["_id"] = str(idc["_id"])
        return(idc)

    def returnEmailFromRegisterar_ID(self,ids):
        from_query = {"_id":ObjectId(ids)}
        field = {"Registerar_Email":1}
        idc = self.collection.find_one(from_query,field)
        del(idc["_id"])
        return(idc["Registerar_Email"])

    def updateMongoDBLoginCredits(self,email,data):
        query = {"Registerar_Email":email}
        field ={"Block_Chain":1}
        collection = self.db[MongoDB_LoginCollectionName]
        chain = collection.find_one(query,field)
        chain=chain['Block_Chain']
        chain[-1]["water_data"]["Self_Data"]["Self_Allowance"] = data[0]
        chain[-1]["water_data"]["Self_Data"]["Self_Credits"] = data[1]
        updateField = {"$set":{"Block_Chain":chain}}
        collection.update_one(query,updateField)
        #print("Wow Ye chal gya")

    def MongDBBlockchainUpgrade(self,email,chain):
        query = {"Registerar_Email":email}
        field ={"Block_Chain":1}
        collection = self.db[MongoDB_LoginCollectionName]
        updateField = {"$set":{"Block_Chain":chain}}
        collection.update_one(query,updateField)
        print("Query = "+ str(query))
        #print(chain)
        print(field)



    def Transaction_Chain(self,from_credit_ID,to_ID,credit_amount):
        #Takes from and to
        #Initializes empty response finds the mongoDB based on objectID If not empty then find to if that too non Empty
        #Then if to credit is less than zero and if from credit is greater than equal to credit credit_amount
        #New extended allowance update allowance and credits of respective
        updated_from = {"Allowance":0,"Credits":0}
        updated_to = {"Allowance":0,"Credits":0}
        response ={"Message":"","Status":False,"Transaction_chain":{"From":f"Failed from {from_credit_ID}",
        "To":f"Failed to {to_ID}","Credits":f"Failed credits:{credit_amount}","TimeStamp":self.GetTimeStamp()}}
        from_query = {"_id":ObjectId(from_credit_ID)}
        field = {"Allowance":1,"Credits":1,"Device_Status":1}
        to_query = {"_id":ObjectId(to_ID)}
        res_from = self.collection.find_one(from_query,field)
        #print(f"From response: {res_from} & len = {len(res_from)} & {res_from is None}")
        if self.isResponseEmpty(res_from) or res_from["Device_Status"]=="Inactive":
            response["Message"] = "Error in from-Device-ID. Please Recheck the Device-ID you have entered is correct and also Device is active."
        else:
            res_to = self.collection.find_one(to_query,field)
            if self.isResponseEmpty(res_from) or res_to["Device_Status"]=="Inactive":
                response["Message"] = "Error in to-Device-ID. Please Recheck the Device-ID you have entered is correct and also Device is active."
            else:
                if res_to["Credits"]<0:
                    if res_from["Credits"] >= credit_amount:
                        extended_Allowance = credit_amount*perCreditAllowance
                        updated_from["Allowance"] = res_from["Allowance"] + extended_Allowance
                        updated_to["Allowance"] = res_to["Allowance"] - (extended_Allowance*cutoffFactor)
                        updated_from["Credits"] = res_from["Credits"] - credit_amount
                        updated_to["Credits"] = res_to["Credits"] + credit_amount
                        self.collection.update_one(from_query,{"$set":updated_from})
                        self.collection.update_one(to_query,{"$set":updated_to})
                        response["Transaction_chain"] = {"From":from_credit_ID,"To":to_ID,"Credits":credit_amount,
                        "TimeStamp":self.GetTimeStamp()}
                        response["Status"] = True
                        response["Message"] = "Transaction success!"
                        from_email = self.returnEmailFromRegisterar_ID(from_credit_ID)
                        to_email = self.returnEmailFromRegisterar_ID(to_ID)
                        self.updateMongoDBLoginCredits(from_email,[updated_from["Allowance"],updated_from["Credits"]])
                        self.updateMongoDBLoginCredits(to_email,[updated_to["Allowance"],updated_to["Credits"]])
                        response["Message"] = f"Process is Successful! Your allowance has extended to {updated_from['Allowance']} Liters/day!"



                    else:
                        response["Message"] = "Your account doesn't have enough credits to perform the transaction."
                else:
                    response["Message"] = "You can't buy services from the industries having drop-coins >= 0."



        return(response)

    def requestUpdate(self,key,IdentificationID,param):
        query={key:IdentificationID}
        field={"$set":param}
        self.collection.update_one(query,field)
        return("Update Success")

    def returnQuery(self,key,field):
        result = self.loginCollection.find_one(key,field)
        if result is None:
            print("Query not found")
        elif len(result)==0:
            print("Query not found")
            return({})
        else:
            del(result["_id"])
            return(result)

    def experimentationFunction(self,senderID):
        pass








        #sheet.update_cell(locate,index+1,"Active")

        #cell = sheet.find("searchCriteria", in_column=1)
#admin_ops.createDevices()
#admin_ops.UpdateDataBaseFromGSheets()
