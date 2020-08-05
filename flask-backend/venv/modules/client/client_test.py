from modules.jsonDump.jsonDumper import JsonLocator
import json,requests
client_secrets_path = r'client_secrets/clientSecrets.json'
def jsonReader(path):
    with open(path) as f:
        data = json.load(f)
    return data
jsonData = jsonReader(client_secrets_path)
blockchainurl ='http://localhost:5000/fetch-client-details'
url = 'http://localhost:5000/device-fetch'
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
        print(res.json())

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

# test = JsonLocator(None)
# print(test.getHourOfDay())
# print(test.getDayofWeek())
# print(test.getMonthofYear())
# print(test.getTodayDate())



cpush = Client_Update()

cpush.serverFetchRequest(jsonData,blockchainurl)
