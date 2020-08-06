import requests,json
from modules.IoT.python_iot import python_IOT as piot
from modules.blockchain.blockchain import Blockchain
from modules.jsonDump.jsonDumper import JsonLocator
client_secrets_path = r'client_secrets/clientSecrets.json'
dummy_json_data_path = r'client_secrets/dummyData.json'
def jsonReader(path):
    with open(path) as f:
        data = json.load(f)
    return data
jsonData = jsonReader(client_secrets_path)
dummyData = jsonReader(dummy_json_data_path)
url = 'http://localhost:5000/device-fetch'
blockchainurl ='http://localhost:5000/blockchain-device'
mineblockurl ='http://localhost:5000/mine-block'
#Fetch data from R-pi every minute and keep averaging it until an hour passes
#Fetch data from R-Pi for 1 hour => Post data to local server {Includes Data + TimeStamp + Hour + Day}
#Local server verify token => If verified allow data posting every hour

class Client_Update:

    def __init__(self):
        self.endpointUrl = url
        self.accessKey = jsonData
        self.connection = False
        self.OCPData = None
        self.SWAData = None
        self.FRCData = None
        self.PLAData = None
        self.RCIData = None
        self.RSIData = None
        self.TSMData = None
        self.RealTimeData = {}
        self.res = {}

    def checkConnection(self):
        res = requests.post(self.endpointUrl, json = self.accessKey)
        return(res.json())

    def updateData(self,realtime_jsonData):
        self.TSMData = realtime_jsonData["time"]
        self.OCPData = self.AverageData(self.OCPData,realtime_jsonData["Optical_Color_Index"])
        self.SWAData = self.AverageData(self.OCPData,realtime_jsonData["Solid_Waste_Analysis_Index"])
        self.FRCData = self.AverageData(self.OCPData,realtime_jsonData["FlowRate"])
        self.PLAData = self.AverageData(self.OCPData,realtime_jsonData["Pressure_Leakage_Alert"])
        self.RCIData = self.AverageData(self.OCPData,realtime_jsonData["Relative_Conductivity"])
        self.RSIData = self.AverageData(self.OCPData,realtime_jsonData["Relative_Spectral_Index"])

    def returnRawData(self):
        OCI_Array = [self.OCPData,self.SWAData,self.PLAData,
        self.RCIData,self.RSIData,self.FRCData,0]
        return(OCI_Array)

    def serverFetchRequest(self,credentials,endpointUrl):
        self.res["email"] = credentials["email"]
        self.res["password"] = credentials["password"]
        self.res["Device_ID"] = credentials["Device_ID"]
        self.res["R_ID"] = credentials["Registerar_ID"]
        res = requests.post(endpointUrl, json = self.res)
        return(res.json())

    # def filterSelf(self,deviceID,records):
    #     for record in records:

    # def PackAndSend(self,hourContext,datapacket):
    #     # datapacket = {"time":self.TSMData,"Optical_Color_Index":self.OCPData,
    #     #                 "Solid_Waste_Analysis_Index":self.SWAData,
    #     #                 "FlowRate":self.FRCData,"Pressure_Leakage_Alert":self.PLAData,
    #     #                 "Relative_Conductivity":self.RCIData,
    #     #                 "Relative_Spectral_Index":self.RSIData,"Hour":hourContext}
    #     res = requests.post(self.endpointUrl, json = datapacket)

    def AverageData(self,existingData,UpcomingData):
        if existingData is None:
            return(UpcomingData)
        else:
            return(0.5*(existingData+UpcomingData))


cpush = Client_Update()
pyIot = piot()
blockchain = Blockchain(jsonData,blockchainurl)
jsonInitial = blockchain.getJsonInitial()
jsonit = JsonLocator(jsonInitial)
industryData = cpush.serverFetchRequest(self,credentials,endpointUrl)
jsonit.Set_02_Values(industryData['Industry'])
jsonit.Set_03_Values(industryData['Self'])

#blockchain.mine_block(dummyData)
#print(blockchain.serverPushRequest(jsonData,mineblockurl))
hour = int(pyIot.GetTimeStamp().split(" ")[1].split(":")[0])
validator = cpush.checkConnection()
msg = validator["Error_Message"]
validator = validator["Is_Valid"]
print("Data Read is active now!")

while validator:
    current_hour = int(pyIot.GetTimeStamp().split(" ")[1].split(":")[0])
    if hour<current_hour:
        print(f"Consolidating @ time = {current_hour}")
        # Averaging code here
        validator = cpush.checkConnection()
        msg = validator["Error_Message"]
        validator = validator["Is_Valid"]
        if not(validator):
            break
        else:
            OCI = pyIot.Compute_RealTime()
            OCI = client_token.updateData(OCI)
            OCI = client_token.returnRawData()
            jsonit.Set_01_Values(OCI)
            '''Processing needs to be done here before running the program'''
            #blockchain.serverPushRequest(jsonData,mineblockurl)
        #verifying response here
        #Re-assigning hour here
        hour = hour + 1
        print(f"Updating time hour = {hour} from hour = {hour-1}")
    else:
        datapacket = pyIot.Compute_RealTime()
        cpush.updateData(datapacket)
print("Connection lost to device or Invalid login Attempt! Error Message:\n\t{msg}")
