import requests,json
from datetime import datetime
#Constants
currentPlaybackurl = 'https://livepeer.com/api/ingest'
objPlayerLink = 'https://obsproject.com/download'
streamUrl = 'https://livepeer.com/api/stream/'
apitokenUrl = 'https://livepeer.com/api/api-token/'

class LivePeer:
    def __init__(self,apiKey,jsonbody):
        self.key = apiKey["key"]
        self.jsonBody = jsonbody
        self.url = 'https://livepeer.com/api/stream'
        self.headers = {
        'Content-type': 'application/json',
        'Authorization': f'Bearer {self.key}'
        }
        self.ingest = ''
        self.playback = ''
        self.streamkey = apiKey["StreamKey"]
        self.playbackId = apiKey["playbackID"]
        self.id = apiKey["id"] #Also known as streamid [For deleting streams]
        self.isStreamingTrue = False
        self.publicUrl = ''
        self.StreamIds = []
        self.AudienceUrl = ''

    def Authorize(self):
        return({'Authorization': f'Bearer {self.key}'})

    def PostRequest(self,url,headers,jsonbody):
        if headers=={}:
            headers=self.headers
        if jsonbody=={}:
            res = requests.post(url,headers=headers)
        else:
            res = requests.post(url,headers=headers,json=jsonbody)
        res = res.json()
        return(res)

    def GetRequest(self,url):
        res = requests.get(url)
        return(res)

    def GetRequestwithHeaders(self,url,Headers):
        res = requests.get(url,headers=Headers)
        return(res)

    def GetIngestAndPlayBackUrl(self,url=currentPlaybackurl):
        res = self.GetRequest(url)
        res = res.json()[-1]
        self.ingest = res["ingest"]
        self.playback = res["playback"]
        return(res)

    def DisplayIngestAndStreamKey(self):
        if self.AudienceUrl=='':
            return("String not configured yet.")
        else:
            return(self.AudienceUrl)

    def CreateStreamObject(self,url=None):
        if url is None:
            url = streamUrl
        if self.ingest=='' or self.playback=='':
            print("Error creating Stream Object... Running GetIngestAnfPlayBackUrl to fetch ingest and playback.")
            res = self.GetIngestAndPlayBackUrl(currentPlaybackurl)

        res = self.PostRequest(self.url,{},self.jsonBody)
        try:
            print(f"Stream Object Details:\n'name':\t{res['name']}\n'kind':\t{res['kind']}\n'createdByTokenName':\t{res['createdByTokenName']}")
            self.streamkey = res['streamKey']
            self.playbackId = res['playbackId']
            self.id = res['id']
            return({"StreamKey":self.streamkey,"playbackId":self.playbackId,"id":self.id})
        except:
            print("Unable to fetch the data from API. Please check all the details used are completely valid")
            return("Invalid Query. Failed to create stream object. Error must be in calling API")

    def DisplayStreamingDetails(self):
        print(f'Go to OBS player or you may download it from here: {objPlayerLink}')
        print('Enter the field details as follows:')
        if self.ingest=='' or self.playback=='':
            print("Error creating Stream Object... Running GetIngestAnfPlayBackUrl() to fetch ingest and playback.")
            res = self.GetIngestAndPlayBackUrl(currentPlaybackurl)
            res = self.CreateStreamObject()
        print(f'Service: \t\tCustom\nServer: \t\t{self.ingest}\nStream Key: \t\t{self.streamkey}\nid: \t\t{self.id}\nplaybackID: \t\t\t{self.playbackId}')

    def FetchStreamStatus(self,id):
        print("Fetching stream status...")
        print(f"ID is: {id}")
        if id == '':
            print("Invalid streaming choice! Please enter the ID.")#removing / at the end
        else:
            url = streamUrl + id
            print(self.Authorize())
            res = self.GetRequestwithHeaders(url,self.Authorize())
            #print(f"\n\n\nres={res}")
            res = res.json()
        if "lastSeen" in res:
            try:
                date = datetime.fromtimestamp(res["lastSeen"]/1000).strftime('%d-%b-%Y %H:%M hrs.')
                print(f"Last seen at {date}")
            except Exception as e:
                print(e)
                print(f"Last Seen TimeStamp: {res['lastSeen']}")
            self.isStreamingTrue = True
        else:
            print('Data not fetched correctly! Please try again')

    def FetchUserUrl(self,playbackId,id):
        self.FetchStreamStatus(id)
        self.GetIngestAndPlayBackUrl()
        url = f'{self.playback}/{playbackId}/index.m3u8'
        self.AudienceUrl = url
        print(f"Verifying Playback Url: {url}\n\n")
        for i in range(3):
            res = self.FetchUserUrlResponse(url)
            print(res)
        return({"Url_Point":self.AudienceUrl})

    def ReturnFetchUserUrl(self):
        if self.playback=='':
            res = self.GetIngestAndPlayBackUrl()
        return({"url":f"{self.playback}/{self.playbackId}/index.m3u8"})



    def FetchUserUrlResponse(self,url):
        res = self.GetRequest(url)
        print(f"status code: {res.status_code}")
        print(f"Response: {res.text}")
        #res = res.json()
        return(res.text)

    def FetchAllStreamIds(self):
        streamIds = []
        headers = self.headers
        del(headers['Content-type'])
        url = f'{apitokenUrl}/{self.key}'
        res = self.GetRequestwithHeaders(url,headers)
        res = res.json()
        #print(res)
        url = f'https://livepeer.com/api/stream/user/{res["userId"]}'
        res = self.GetRequestwithHeaders(url,headers)
        objects = res.json()
        #print(objects)
        for object in objects:
            streamIds.append(object["id"])
        self.StreamIds = streamIds
        return(streamIds)

    def DeleteRequest(self,url,headers):
        if headers=={}:
            headers=self.headers
        res = requests.delete(url,headers=headers)
        res = res.json()
        return(res)

    def DeleteStreams(self,idx=False):
        self.FetchAllStreamIds()
        if idx==False:
            for i in self.StreamIds:
                url = f"{streamUrl}{i}"
                self.DeleteRequest(url,self.Authorize())
                print(f"Stream Deleted for {i}")
            self.StreamIds = []
        else:
            url = f"{streamUrl}{idx}"
            headers = self.headers
            del(headers['Content-type'])
            DeleteRequest(url,headers)
