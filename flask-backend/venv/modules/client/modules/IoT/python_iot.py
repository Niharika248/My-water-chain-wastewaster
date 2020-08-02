#python-iot
import datetime
from random import random

##Constant Definition
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
class python_IOT:
    def __init__(self):
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
        self.CurrentPointer = 0
        self.th = th
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
        datapacket = {"time":self.GetTimeStamp(),"Optical_Color_Index":self.OCPIndex(),
                        "Solid_Waste_Analysis_Index":self.SWAIndex(),
                        "FlowRate":self.FlowRate(),"Pressure_Leakage_Alert":self.PLA(),
                        "Relative_Conductivity":self.RC_Index(),
                        "Relative_Spectral_Index":self.RS_Index()}
        return(datapacket)
    def AnalysisBoolean(self):
        for i in range(self.ValidationCheck):
            if self.OCPIndex() not in range(int(self.OCP-self.th),int(self.OCP+self.th)) or self.SWAIndex() not in range(int(self.SWA-self.th),int(self.SWA+self.th)) or self.FlowRate() not in range(int(self.FRC-self.th),int(self.FRC+self.th)) or self.FlowRate() not in range(int(self.FRC-self.th),int(self.FRC+self.th)) or self.PLA() not in range(int(self.PLS-self.th),int(self.PLS+self.th)) or self.RC_Index() not in range(int(self.RCK-self.th),int(self.RCK+self.th)) or self.RS_Index() not in range(int(self.RSK-self.th),int(self.RSK+self.th)):
                pass
            else:
                return True
            return False
    def ShowPresentData(self):
        print(f"TimeStamp = {self.TimeStamp}\t\tOCP = {self.OCP}\nSWA = {self.SWA}\t\tFRC = {self.FRC}\nPLS = {self.PLS}\tRCK = {self.RCK}\n\tRSK = {self.RSK}")
    def returnJSON(self):
        return self.jsonPacket
##reference = python_IOT()
##
##for i in range(numberOfPacketstoRecieve*dataPacket+1):
##    reference.Compute_RealTime()
##dataFetched = reference.returnJSON()
##print(dataFetched)
