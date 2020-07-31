import uuid 

class ElementorDetails:
    def __init__(self):
        self.data={}
        self.embed(deviceID=uuid.uuid1(),registeredName="",registeredEmail="",woName="",
                   woEmail="",Score={"OCP":0,"SWA":0,"FRBPL":0,"CF":0,"SA":0},message="",sensorStatus="")
    def 
