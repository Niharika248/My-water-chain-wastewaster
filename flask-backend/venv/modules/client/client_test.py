import requests,json
from modules.IoT.python_iot import python_IOT as piot
from modules.blockchain.blockchain import Blockchain
from modules.jsonDump.jsonDumper import JsonLocator
client_secrets_path = r'client_secrets/clientSecrets.json'

def jsonReader(path):
    with open(path) as f:
        data = json.load(f)
    return data
jsonData = jsonReader(client_secrets_path)

chain_URL = 'http://localhost:5000/client-fetch-chain'
previous_chain = 'http://localhost:5000/xnodscdshfewhfewdshef'
mine_block_URL = 'http://localhost:5000/mine-block'
class ClientData:
    def __init__(self,data):
        self.loginID = data["Device_ID"]
        self.Registerar_ID = data["Registerar_ID"]
        self.Email_ID = data["email"]
        self.password = data["password"]
        self.ChainUrl = chain_URL
        self.previouschainurl = previous_chain
        self.rawJson = data
        self.chain = []
        self.OCPData = None
        self.SWAData = None
        self.FRCData = None
        self.PLAData = None
        self.RCIData = None
        self.RSIData = None
        self.TSMData = None
        self.RealTimeData = {}


    def ValidateResponse(self):
        response = self.PostRequest(self.ChainUrl,self.rawJson)
        response = response.json()
        if response["Is_Valid"]:
            return(True)
        else:
            print(f"Invalid operation. Error Message: {repsonse['Error_Message']}")
            return(False)

    def getPreviousChain(self):
        #1. Verify the client_token
        #2. return the chain
        if self.ValidateResponse():
            key = {"Registerar_Email":self.Email_ID}
            field = {"Block_Chain":1}
            validationPacket = {"Validate":self.rawJson}
            result = self.PostRequest(self.previouschainurl,{"key":key,"field":field,"encrypt":validationPacket})
            self.chain = result.json()["Block_Chain"]
            return(True)
        else:
            return(False)


    def PostRequest(self,requesturl,requestjson):
        response = requests.post(requesturl, json = requestjson)
        return(response)

    def AverageData(self,existingData,UpcomingData):
        if existingData is None:
            return(UpcomingData)
        else:
            return(0.5*(existingData+UpcomingData))

    def returnRawData(self):
        OCI_Array = [self.OCPData,self.SWAData,self.PLAData,
        self.RCIData,self.RSIData,self.FRCData,0]
        return(OCI_Array)

    def updateData(self,realtime_jsonData):
        self.TSMData = realtime_jsonData["time"]
        self.OCPData = self.AverageData(self.OCPData,realtime_jsonData["Optical_Color_Index"])
        self.SWAData = self.AverageData(self.OCPData,realtime_jsonData["Solid_Waste_Analysis_Index"])
        self.FRCData = self.AverageData(self.OCPData,realtime_jsonData["FlowRate"])
        self.PLAData = self.AverageData(self.OCPData,realtime_jsonData["Pressure_Leakage_Alert"])
        self.RCIData = self.AverageData(self.OCPData,realtime_jsonData["Relative_Conductivity"])
        self.RSIData = self.AverageData(self.OCPData,realtime_jsonData["Relative_Spectral_Index"])

    def Mine_Block(self,mine_block_url,block):
        res = self.PostRequest(mine_block_url,{"block":block,"credentials":self.rawJson})



client_token = ClientData(jsonData)
client_token.getPreviousChain()
client_chain = Blockchain(client_token.chain)

pyIot = piot()
jsonInitial = client_chain.getJsonInitial()
jsonit = JsonLocator(jsonInitial)

hour = int(pyIot.GetTimeStamp().split(" ")[1].split(":")[0])
validator = client_token.ValidateResponse() and client_chain.is_chain_valid()

if validator:
    print("Data Read is active now!")
    OCI = pyIot.Compute_RealTime()
    OCI = client_token.updateData(OCI)
    OCI = client_token.returnRawData()
    jsonit.Set_01_Values(OCI)
    #print(jsonit.jsonFile)
    client_chain.mine_block(jsonit.jsonFile)
    if client_chain.is_chain_valid():
        client_token.Mine_Block(mine_block_URL,client_chain.chain)

    else:
        print("Invalid Chain")
else: print("Aborting...")




# while validator:
#     current_hour = int(pyIot.GetTimeStamp().split(" ")[1].split(":")[0])
#     if hour<current_hour:
#         print(f"Consolidating @ time = {current_hour}")
#         # Averaging code here
#         validator = client_token.ValidateResponse() and client_chain.is_chain_valid()
#         if not(validator):
#             print("Aborting...")
#             break
#         else:
#             OCI = pyIot.returnJSON()
#             OCI = client_token.updateData(OCI)
#             OCI = client_token.returnRawData()
#             jsonit.Set_01_Values(OCI)
#             industryData = cpush.serverFetchRequest(self,credentials,endpointUrl)
#             '''Processing needs to be done here before running the program'''
#             #blockchain.serverPushRequest(jsonData,mineblockurl)
#         #verifying response here
#         #Re-assigning hour here
#         hour = hour + 1
#         print(f"Updating time hour = {hour} from hour = {hour-1}")
#     else:
#         datapacket = pyIot.Compute_RealTime()
#         cpush.updateData(datapacket)
# print("Connection lost to device or Invalid login Attempt! Error Message:\n\t{msg}")
