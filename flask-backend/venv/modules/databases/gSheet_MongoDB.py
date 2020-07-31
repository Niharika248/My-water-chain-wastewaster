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
createDevice_MessageCode = 'TRUE'
update_MessageCode = 'Updated'
AdminPasswordChangeRequest = 'AdminPasswordChange'
AdminPasswordChangeHeader = 'PasswordChange'
MongoDBPasswordField = 'Password'
PasswordChangeStaticName = update_MessageCode

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
        self.worksheet = self.sh.sheet1
        self.bulksheet = self.sh.worksheet(bulk_associate_sheet_name)
    def getMongoDBCollection(self,collectionName):
        return(self.db[collectionName])
    def gSheetReflect(self):
        #This function reads the sheet and accordingly reflects the value in Mongo Database
        Headers = self.worksheet.row_values(1) #Header indexing starts from 1 and not 0.
        Device_Status_Index = Headers.index(DeviceStatusHeading)
        print(f"Reflecting changes based on {Headers[Device_Status_Index]}")
    def GetTimeStamp(self):
        timestamp = str(datetime.datetime.now()).split(":")
        try:return(timestamp[0]+":"+timestamp[1]+ " hrs")
        except: return(str(datetime.datetime.now()))
    def GetIndexByHeader(self,HeaderString,sheetType):
        Headers = sheetType.row_values(1)
        return(Headers.index(HeaderString))
    def createDevices(self):
        newEntries = self.bulksheet.get_all_records()[0:]
        StatusIndex = self.GetIndexByHeader("Status",self.bulksheet)
        cellEntry = 0
        for entry in newEntries:
            if entry["Status"]==createDevice_MessageCode:
                pass
            else:
                timestamp = self.GetTimeStamp()
                _id = self.collection.insert({"Registerar_UserName":entry["Registerar_UserName"],
                                         "Registerar_Email":entry["Registerar_Email"],
                                         "Organisation_Name":entry["Organisation_Name"],
                                         "Organisation_Email":entry["Organisation_Email"],
                                         "Allowance":entry["Allowance"],
                                         "Device_Status":"Inactive",
                                         "TimeStamp":timestamp})
                data = [str(_id),entry["Registerar_UserName"],entry["Registerar_Email"],
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
                                     "Device_Status":"Inactive",
                                     "TimeStamp":timestamp}
                self.collection.update({"_id":ObjectId(entry["Device_ID"])},{"$set":newdata})
                self.worksheet.update_cell(rownum,StatusIndex+2,timestamp)
                self.worksheet.update_cell(rownum,StatusIndex+1,"Updated")
            rownum+=1
    def LoginDetailsUpdate(self,details,isAdd,collectionType,sheetType,globalSheetName):
        if isAdd:
            collection = self.db[collectionType]
            details["TimeStamp"] = self.GetTimeStamp()
            _id = collection.insert(details)
            data = [str(_id),details["Device_ID"],details["Registerar_Email"],details["TimeStamp"],PasswordChangeStaticName]
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
                
    
        #sheet.update_cell(locate,index+1,"Active")
        
        #cell = sheet.find("searchCriteria", in_column=1)
#admin_ops.createDevices()
#admin_ops.UpdateDataBaseFromGSheets()


