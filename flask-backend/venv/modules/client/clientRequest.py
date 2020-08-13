import requests,json,hashlib
from random import random
from modules.IoT.python_iot import python_IOT as piot
from modules.blockchain.blockchain import Blockchain
from modules.jsonDump.jsonDumper import JsonLocator
from time import sleep
import datetime
client_secrets_path = r'client_secrets/clientSecrets.json'
quantityConstant = 1
qualityConstant = 1
import time
def jsonReader(path):
    with open(path) as f:
        data = json.load(f)
    return data

jsonData = jsonReader(client_secrets_path)
ipaddress = 'http://192.168.56.1:5000/'
verifyUrl = f'{ipaddress}client-fetch-chain'
previous_chain = f'{ipaddress}xnodscdshfewhfewdshef'
mine_block_URL = f'{ipaddress}mine-block'
validate_chain_and_upload_url = f'{ipaddress}validate-chain-and-upload'

###########################################################################IoT Constants######################################################################
dataPacket = 30000
numberOfPacketstoRecieve = 10
validationCheck = 50
OCPConstant = 5
SWAConstant = 6
FRConstant = 160
PLSConstant = 1.5
RCK = 1
RSK = 1.2
th = 1.2
###########################################################################IoT Constants######################################################################

class BIoT: #Blockchain + IoT

    def __init__(self,jsonData):
        self.chain = []
        self.TimeStamp = ""
        self.OCP = OCPConstant
        self.SWA = SWAConstant
        self.FRC = FRConstant
        self.PLS = PLSConstant
        self.RCK = RCK
        self.RSK = RSK
        self.jsonPacket = []
        self.dataPacket = dataPacket
        self.ValidationCheck = validationCheck
        self.OCPData = None
        self.SWAData = None
        self.FRCData = None
        self.PLAData = None
        self.RCIData = None
        self.RSIData = None
        self.TSMData = None
        self.th = th
        self.credentials = jsonData
        self.jsonFile = {}
        self.today = datetime.datetime.now()
        self.qualityConstant = 1
        self.quantityConstant = 1
#######################################################################Networking##############################################################################
    def FetchFirstChain(self):
        #Goto Server and request chain after validationCheck

        key = {"Registerar_Email":self.credentials["email"]}
        field = {"Block_Chain":1}
        validationPacket = {"Validate":self.credentials}
        result = self.PostRequest(previous_chain,{"key":key,"field":field,"encrypt":self.credentials})
        if result.json()["Is_Valid"]:
            self.chain = result.json()["Block_Chain"]
            self.jsonFile = self.chain[-1]["water_data"]
            #print(jsonFile)
            return(True)
        else:
            print(reuslt.json()["Error_Message"])

    def PostRequest(self,url,jsonbody):
        response = requests.post(url,json=jsonbody)
        return(response)


    def create_block(self, proof, previous_hash,waterdata):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'water_data':waterdata}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def mine_block(self,waterdata):
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        block = self.create_block(proof, previous_hash,waterdata)

    def is_chain_valid(self):
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            #print(f"current: {block['previous_hash']} for index = {block['index']}")
            #print(f"previous hash: {previous_block['previous_hash']} for index = {previous_block['index']}")
            if block['previous_hash'] != self.hash(previous_block):
                #print(f"{block['previous_hash']} is not equal to {self.hash(previous_block)}")
                #print("Previous hash of the block isn't equal to the previous hash. Chain disrupted. This is a bad news :-(")
                #print(f"In valididty is caused for the block index: {block_index}")
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                print("This goes wrong")
                return False
            previous_block = block
            block_index += 1
        #print(f"{block['previous_hash']} is equal to {self.hash(previous_block)}")
        return True


###############################################################################IoT Part#########################################################################################
    def GetTimeStamp(self):
        timestamp = str(datetime.datetime.now()).split(":")
        try:return(timestamp[0]+":"+timestamp[1]+ " hrs")
        except: return(str(datetime.datetime.now()))

    def OCPIndex(self):
        return(round(random()*OCPConstant,2))

    def SWAIndex(self):
        return(round(random()*SWAConstant,2))

    def FlowRate(self):
        return(round(random()*FRConstant,2))

    def PLA(self):
        return(round(random()*PLSConstant,2))

    def RC_Index(self):
        return(round(random()*RCK,2))

    def RS_Index(self):
        return(round(random()*RSK,2))

    def Compute_RealTime(self):
        self.TSMData = self.GetTimeStamp()
        self.OCPData = self.OCPIndex()
        self.SWAData = self.SWAIndex()
        self.FRCData = self.FlowRate()
        self.PLAData = self.PLA()
        self.RCIData = self.RC_Index()
        self.RSIData = self.RS_Index()
        datapacket = [self.OCPData,self.SWAData,self.FRCData,
        self.PLAData,self.RCIData,self.RSIData,0,self.TSMData]
        return(self.updateData(datapacket))


    def ShowPresentData(self):
        print(f"TimeStamp = {self.TimeStamp}\t\tOCP = {self.OCP}\nSWA = {self.SWA}\t\tFRC = {self.FRC}\nPLS = {self.PLS}\tRCK = {self.RCK}\n\tRSK = {self.RSK}")

    def AverageData(self,existingData,UpcomingData):
        if existingData is None:
            return(UpcomingData)
        else:
            return(0.5*(existingData+UpcomingData))

    def updateData(self,realtime_jsonData):
        self.TSMData = realtime_jsonData[7]
        #print(f"{realtime_jsonData[0]} and {self.OCPData}")
        self.OCPData = self.AverageData(self.OCPData,realtime_jsonData[0])
        self.SWAData = self.AverageData(self.SWAData,realtime_jsonData[1])
        self.FRCData = self.AverageData(self.FRCData,realtime_jsonData[2])
        self.PLAData = self.AverageData(self.PLAData,realtime_jsonData[3])
        self.RCIData = self.AverageData(self.RCIData,realtime_jsonData[4])
        self.RSIData = self.AverageData(self.RSIData,realtime_jsonData[5])
        datapacket = [self.OCPData,self.SWAData,self.FRCData,
        self.PLAData,self.RCIData,self.RSIData,0,self.TSMData]
        return(datapacket)

########################################################################## Json Program   ##########################################################################################
    def Set_01_Values(self,OCI,hour):
        #hour = self.getHourOfDay()
        self.jsonFile["Optical_Color_Index"][hour] = OCI[0]
        self.jsonFile["Quality_Analysis"]["HSI"] = OCI[0]
        self.jsonFile["Quality_Analysis"]["SWI"] = OCI[1]
        self.jsonFile["Quality_Analysis"]["CDI"] = OCI[3]
        self.jsonFile["Quality_Analysis"]["SPI"] = OCI[4]
        # self.jsonFile["Water_Quality_Index_Day"][hour] = (self.qualityConstant*((OCI[3]*OCI[4])/(OCI[1]*OCI[2])))
        # self.jsonFile["Water_Quantity_Index_Day"][hour] = (self.qualityConstant*OCI[5])
        self.jsonFile["Solid_Waste_Analysis_Index"][hour] = OCI[1]
        self.jsonFile["Pressure_Leakage_Alert"][hour] = OCI[2]
        self.jsonFile["Relative_Conductivity"][hour] = OCI[3]
        self.jsonFile["Relative_Spectral_Index"][hour] = OCI[4]
        self.jsonFile["FlowRate"][hour] = OCI[5]
        if len(self.jsonFile["Credit_Consumption_History"])<=self.getMonthofYear():
            for i in range(len(self.jsonFile["Credit_Consumption_History"]),self.getMonthofYear()):
                self.jsonFile["Credit_Consumption_History"].append(0)

        self.jsonFile["Credit_Consumption_History"][self.getMonthofYear()-1]+=OCI[6] #OCI-06 is always 0 unless a purchase is confirmed

    def getHourOfDay(self):
        return(int(str(self.today).split(" ")[1].split(":")[0]))

    def getDayofWeek(self):
        return(self.today.weekday())

    def getMonthofYear(self):
        return(self.today.month)

    def getTodayDate(self):
        timestamp = self.today.timestamp()
        timestamp = timestamp+(60*60*24*30*3)
        newDate = datetime.datetime.fromtimestamp(timestamp)
        return(datetime.datetime.strptime(str(newDate).split(" ")[0], "%Y-%m-%d").strftime("%d-%B-%Y"))

    def ValidateResponse(self):
        response = self.PostRequest(verifyUrl,self.credentials)
        response = response.json()
        if response["Is_Valid"]:
            return(True)
        else:
            print(f"Invalid operation. Error Message: {repsonse['Error_Message']}")
            return(False)

    def PostRequest(self,requesturl,requestjson):
        response = requests.post(requesturl, json = requestjson)
        return(response)

##########################################################################   Main Program ##########################################################################################

biot = BIoT(jsonData)
print(f" success Status: {biot.FetchFirstChain()}")
statusMessage="All good!" if biot.is_chain_valid() else "Something is not right with your blockchain, Please contact your administrator"
print(statusMessage)
hour = int(biot.GetTimeStamp().split(" ")[1].split(":")[0])
minute = int(biot.GetTimeStamp().split(" ")[1].split(":")[1])
validator = biot.ValidateResponse()

while validator:
    current_minute = int(biot.GetTimeStamp().split(" ")[1].split(":")[1])
    data = biot.Compute_RealTime()
    for i in range(10):
    # if current_minute > minute:
        minute+=1
        biot.Set_01_Values(data,3)
        print("Mining block: ")
        biot.mine_block(biot.jsonFile)
        print(f" Now chain length = {len(biot.chain)}")
        request = {"chain":biot.chain,"credentials":biot.credentials}
        response = biot.PostRequest(validate_chain_and_upload_url,request)
        print(response)
