import datetime

class JsonLocator:
    def __init__(self,jsonInitial):

        self.today = datetime.datetime.now()
        self.jsonFile = jsonInitial
        self.qualityConstant = 1
        self.quantityConstant = 1

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
