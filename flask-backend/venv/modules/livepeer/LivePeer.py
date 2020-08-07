import requests
import cv2
import base64
import datetime
def configureKeys(path):
    with open(path) as f:
        data = json.load(f)
    return data

class LivePeer:
    def __init__(self,api):
        self.apiKey = api

    def streamAPIresponse(self,url,request,api,postRequest):
        if postRequest:
            response = requests.post(url,json = request)
        else:
            response = requests.get(url,requestbody)

        return(response)

    def SendForStreaming(self,encoded_frame):
        #Get the encoded encoded_frame
        #send the response to client on request

    def RequestStream(self,apiKey):
        #is apiKey valid?
        #if yes recieve the encoded frame to the user in bytes

    def Prepare_Frame(self,frame):
        retval, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        jsonData = {"Encoded_Frame":jpg_as_text,"TimeStamp":datetime.datetime.now()}
        return(jsonData)



credentials_path = r"livepeercredentials.json"
apiKey = configureKeys(credentials_path)
client = LivePeer.streamAPIresponse(apiKey)

cam = cv2.VideoCapture(0)

while True:
    _,frame = cam.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
        jsondictionary = client.Prepare_Frame(frame)
        #Send this frame to client for streaming
        #client.SendForStreaming()
