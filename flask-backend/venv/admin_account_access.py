#Importing Useful Libraries
import gspread
import pandas as pd
import pymongo
import datetime
from bson.objectid import ObjectId

#Useful Config Variables

#Service Account Json: You get this from your google's developer console.You can follow this link below to generate yours:
#https://console.cloud.google.com/?pli=1
service_account_json_path = r'google_credentials.json'
#This key is found in your spreadsheet url:
#https://docs.google.com/spreadsheets/d/<gSheetKey>/edit#gid=0
gSheetKey = '1kPUQiO-hlIoQPclmQsJba4B_HW7W8ehspxWPz2z7re4'
DeviceStatusHeading = 'Device_Status' #To locate the header for device status (by index)

#Setting up the environment

#Google Sheet
gc = gspread.service_account(filename = service_account_json_path)
sh = gc.open_by_key(gSheetKey)
worksheet = sh.sheet1
bulksheet =  sh.worksheet('bulk_associate')
#MongoDB
client = pymongo.MongoClient("mongodb+srv://admin-user:ogimljVnqPClQI5i@cluster0-8qxz0.mongodb.net/mywatertech?retryWrites=true&w=majority")
db = client["mywatertech"]
collection = db["userdetails"]


#different ways to fetch data:
#res = worksheet.get_all_records()
#res = worksheet.get_all_values()
#res = worksheet.col_values()
#res = worksheet.get('A2:C2')

class AdminDataBase:
    def __init__(self):
        self.operation=0 #Operation 0 refers to additional database
        self.Device_Status_Index = 6 #Initial Device Status
        self.NumberOfDevices = 0 #Number of Devices to create
        self.EmailAssociation = False #Getting
    def gSheetReflect(self):
        #This function reads the sheet and accordingly reflects the value in Mongo Database
        Headers = worksheet.row_values(1) #Header indexing starts from 1 and not 0.
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
        newEntries = bulksheet.get_all_records()[0:]
        StatusIndex = self.GetIndexByHeader("Status",bulksheet)
        cellEntry = 0
        for entry in newEntries:
            if entry["Status"]=="TRUE":
                pass
            else:
                timestamp = self.GetTimeStamp()
                _id = collection.insert({"Registerar_UserName":entry["Registerar_UserName"],
                                         "Registerar_Email":entry["Registerar_Email"],
                                         "Organisation_Name":entry["Organisation_Name"],
                                         "Organisation_Email":entry["Organisation_Email"],
                                         "Allowance":entry["Allowance"],
                                         "Device_Status":"Inactive",
                                         "TimeStamp":timestamp})
                data = [str(_id),entry["Registerar_UserName"],entry["Registerar_Email"],
                        entry["Organisation_Name"],entry["Organisation_Email"],
                        entry["Allowance"],"Inactive","Updated",timestamp]
                print(data)
                #worksheet.insert_row(data,rownumber=3)
                worksheet.append_row(data)
                bulksheet.update_cell(cellEntry+2,StatusIndex+1,"TRUE")
            cellEntry+=1
    def UpdateDataBaseFromGSheets(self):
        newEntries = worksheet.get_all_records()[0:]
        StatusIndex = self.GetIndexByHeader("Update_Status",worksheet)
        rownum=2
        for entry in newEntries:
            if entry["Update_Status"]=="Updated":pass
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
                collection.update({"_id":ObjectId(entry["Device_ID"])},{"$set":newdata})
                worksheet.update_cell(rownum,StatusIndex+2,timestamp)
                worksheet.update_cell(rownum,StatusIndex+1,"Updated")
            rownum+=1
#admin_ops.createDevices()
#admin_ops.UpdateDataBaseFromGSheets()


