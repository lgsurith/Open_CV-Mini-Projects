import time
import math
import cv2 as cv
import numpy as np
import mediapipe as mp
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#setting up / resizing the window size.
wcam , hcam = 640 , 480

cam = cv.VideoCapture(0)
cam.set(3,wcam)
cam.set(4,hcam)
prev_time = 0

#initialisation for drawing hands.
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence = 0.7)
mpDraw = mp.solutions.drawing_utils

x1,x2,y1,y2 = 0,0,0,0

#pycaw implementation.
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volume_range = volume.GetVolumeRange()   #(-65.25, 0.0, 0.03125)
minimum_volume = volume_range[0]
maximum_volume = volume_range[1]

while True:
    success , img = cam.read()
    imgRGB = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    #hand tracking using mediapipe
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id , lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx , cy = int(lm.x*w) , int(lm.y*h)
                if id in [4,8]:
                    if(id==4):
                        x1,y1 = cx , cy
                        cv.circle(img , (x1,y1) , 10 , (0,0,0) , cv.FILLED)
                    if(id==8):
                        x2,y2 = cx , cy
                        cv.circle(img , (x2,y2) , 10 , (0,0,0),cv.FILLED)
                    cv.line(img, (x1,y1) , (x2,y2) , ( 0,0,0) , 3 )
                    cx1,cy1 = (x1+x2)//2 , (y1+y2)//2
                    cv.circle(img , (cx1,cy1) , 10 , (0,0,0) , cv.FILLED)
                    length = math.hypot(x2 - x1 , y2 - y1)

                    #can change using pycaw 
                    #50-300 max and min -65-0
                    vol = np.interp(length , [50,300] , [minimum_volume , maximum_volume])
                    print(int(length) , vol)
                    volume.SetMasterVolumeLevel(vol, None)

                    #giving a button like a feel.
                    if length < 50 :
                        cv.circle(img , (cx1,cy1) , 10 , (0,255,0) , cv.FILLED)

            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    #fps calculation
    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time

    cv.putText(img , f'FPS : {int(fps)}' , (20,60) , cv.FONT_HERSHEY_COMPLEX , 1 , (0 , 0 , 0) , 3 )

    cv.imshow('Img' , img)
    if cv.waitKey(1) & 0xFF == ord('k'):
        break