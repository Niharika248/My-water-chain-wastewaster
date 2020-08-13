import cv2
import numpy as np
from time import sleep
from random import randint as ri
from random import uniform
from os.path import join
x = 640
y = 480
k_x = 40
Coods_FlowRate = [(int(x/10)-k_x,30),(int(x/10)+150-k_x,60)]
Coods_Classification = [(int(x/10)+170-k_x,30),(int(x/10)+290-k_x,60)]
Coods_SolidWasteIndex = [(int(x/10)+310-k_x,30),(int(x/10)+410-k_x,60)]
ky = 30
k_y = 10
x_off = 30
font = cv2.FONT_HERSHEY_SIMPLEX
Coods_FlowRate_Header = [(int(x/10)-k_x,ky-k_y),(int(x/10)+150-k_x-x_off,ky)]
Coods_Classification_Header = [(int(x/10)+170-k_x,ky-k_y),(int(x/10)+290-k_x-x_off,ky)]
Coods_SolidWasteIndex_Header = [(int(x/10)+310-k_x,ky-k_y),(int(x/10)+410-k_x-x_off,ky)]

HeaderArray = ["Flow Rate","Classification","Solid Index"]
TestingArray = ["Waste Water","Fresh Water","Drinking Water"]
TestingProb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1]
k_x_off = 8
k_y_off = 8
HeaderCoods = [(int(x/10)-k_x+k_x_off,ky-k_y+k_y_off),(int(x/10)+170-k_x+k_x_off,ky-k_y+k_y_off),(int(x/10)+310-k_x+k_x_off,ky-k_y+k_y_off)]
k_x_off = 10
k_y_off = 20
BodyCoods = [(int(x/10)-k_x+k_x_off,30+k_y_off),(int(x/10)+170-k_x+k_x_off,30+k_y_off),(int(x/10)+310-k_x+k_x_off,30+k_y_off)]
colorDisplayBox = (0,0,0)
colorHeaderBox = (0,255,255)
colorHeaderText = (0,0,0)
colorDisplayText = (255,255,255)
HeaderFontSize = 0.3
BodyFontSize = 0.35
HeaderFontThickness = 1

#ROI Co-ordinates
ROIColor = (0,0,0)
ROIHeader = (0,255,255)
k_x_off = 80
k = 60
ki=35
k_y_off=10
ROIBoxCood = [(int(x/10)+k_x_off+3*ki,int(y/2)-k_y_off),(int(x/10)+k_x_off+int(2.5*k)+20,int(y/2)+k-20)]
kyy = 16
ROITextBox = [(int(x/10)+k_x_off+3*ki,int(y/2)-k_y_off-kyy),(int(x/10)+k_x_off+int(2.5*k)+20,int(y/2)-k_y_off)]
kxx = 4
ROITextCod = (int(x/10)+k_x_off+3*ki+kxx,int(y/2)-k_y_off-kyy+int(3*kxx))
ROIHeader = "ROI"
ROIHeaderColor = (0,0,0)
ROIHeaderBoxColor = (0,255,255)
ROIHeaderSize = 0.4
ROILineThickness = 2
ROIHeaderFontThickness = 1
storage = r'LivePeerAssets/streaming_assets/'
class ComputerVision:

    def __init__(self,file):
        self.camera = cv2.VideoCapture(file)

    def StreamVideo(self):
        _,frame = self.camera.read()
        frame = cv2.resize(frame,(640,480))
        cv2.imshow("Frame",frame)
        #sleep(5)
        count = 0
        while True:
            _,frame = self.camera.read()
            if cv2.waitKey(1) == ord('q') and 0xFF or _==False:
                print("Exiting")
                break
            else:
                sleep(0.05)
                frame = cv2.resize(frame,(640,480))
                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                frame = self.ImposeBoxFormat(Coods_FlowRate,frame,colorDisplayBox)
                frame = self.ImposeBoxFormat(Coods_Classification,frame,colorDisplayBox)
                frame = self.ImposeBoxFormat(Coods_SolidWasteIndex,frame,colorDisplayBox)
                frame = self.ImposeBoxFormat(Coods_FlowRate_Header,frame,colorHeaderBox)
                frame = self.ImposeBoxFormat(Coods_Classification_Header,frame,colorHeaderBox)
                frame = self.ImposeBoxFormat(Coods_SolidWasteIndex_Header,frame,colorHeaderBox)
                for i in range(len(HeaderArray)):
                    frame = self.ImposeTextFormat(HeaderCoods[i],frame,colorHeaderText,HeaderArray[i],HeaderFontSize,HeaderFontThickness)
                    #print(HeaderCoods[i],colorHeaderText,HeaderArray[i],HeaderFontSize,HeaderFontThickness)

                rawval = self.SensorValues()
                print(rawval)
                for i in range(len(BodyCoods)):
                    #print(f" values = {BodyCoods[i]},{colorDisplayText},{rawval[i]},{HeaderFontSize},{HeaderFontThickness}")
                    frame = self.ImposeTextFormat(BodyCoods[i],frame,colorDisplayText,rawval[i],BodyFontSize,HeaderFontThickness)

                frame = self.ImposeBoxFormat(ROITextBox,frame,ROIHeaderBoxColor)
                frame = self.ImposeTextFormat(ROITextCod,frame,ROIHeaderColor,ROIHeader,ROIHeaderSize,ROIHeaderFontThickness)
                frame = self.ImposeBoxFormat(ROIBoxCood,frame,ROIColor,ROILineThickness)
                ret,gray = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
                gray = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
                finalframe = np.hstack((frame,gray))
                cv2.imwrite(join(storage,str(count+1)+".png"),finalframe)
                count+=1
                cv2.imshow("Frame",finalframe)

    def ImposeBoxFormat(self,Coods,frame,color,thickness = cv2.FILLED):

        img = cv2.rectangle(frame, Coods[0], Coods[1], color,thickness)
        return(img)

    def ImposeTextFormat(self,Coods,frame,color,string,fontScale=1,thickness=2):
        img = cv2.putText(frame, string, Coods, font,fontScale, color, thickness, cv2.LINE_AA)
        return(img)

    def SensorValues(self):
        flowRateValue = f"{ri(1000,20000)} sq. pixels/frame"
        waterTypeValue = TestingArray[TestingProb[ri(0,len(TestingProb)-1)]]
        SolidIndexValue = str(round(uniform(0,1)*6,2))
        return([flowRateValue,waterTypeValue,SolidIndexValue])


path = r'LivePeerAssets/videos/sample.mp4'
object = ComputerVision(path)
object.StreamVideo()
