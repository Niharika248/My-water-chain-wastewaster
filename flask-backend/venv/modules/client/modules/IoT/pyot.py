#This is the code to select ROI create background image and note the threshold value for the image
#Note that in our project the camera remains static


#Importing the libraries
import cv2
import  numpy as np

#defining Video Object
cam=cv2.VideoCapture("demovideo.mp4")


#Will be taking first image as background
_,frame=cam.read()
nm=cv2.resize(frame,(640,480)).copy() #Resizing to default camera size
ROI_Index = [97,36,203,39]

while True:
    _,frame=cam.read()
    if not(_):
        break
    frame=cv2.resize(frame,(640,480))
    subtraction=cv2.cvtColor(cv2.absdiff(frame[ROI_Index[0]:ROI_Index[0]+ROI_Index[1],
    ROI_Index[2]:ROI_Index[2]+ROI_Index[3]],nm[97:97+36,203:203+39]),cv2.COLOR_BGR2GRAY)
    _,thresh11 = cv2.threshold(subtraction,20,255,cv2.THRESH_BINARY)
    print(f"Pixel variation frame by frame: {cv2.countNonZero(thresh11)}sq pixels/s.")
    cv2.imshow("Thresh11",thresh11)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("Breaking")
        break
    elif cv2.waitKey(1)==ord('r'): #Press r to select ROI
        x,y,w,h=cv2.selectROI(frame,False)
        print(x,y,w,h)
    else:

        try:
            newimage=frame[y:y+h,x:x+w]
            cv2.imshow("newImage",newimage)
            cv2.imshow("Frame",frame)
        except:
            #cv2.imshow("Frame",cv2.cvtColor(frame,cv2.COLOR_BGR2HSV))
            cv2.imshow("Frame",frame)
#ROI obtained from the above code is: [x=203 y=97 w=39 h=36] the value for [demovideo2=574 106 40 32]
#In case the camera position is changed the following code can have a different ROI as well
