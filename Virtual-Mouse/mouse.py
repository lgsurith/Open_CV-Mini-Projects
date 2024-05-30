import cv2 as cv
import numpy as np
import mediapipe as mp
import time 
# import autopy


mpHands = mp.solutions.hands
hands = mpHands.Hands()
#to draw the lines on the hand detected.
mpDraw = mp.solutions.drawing_utils

wcam , hcam = 640 , 480

cam = cv.VideoCapture(0)
cam.set(3,wcam)
cam.set(4,hcam)
prev_time = 0

while True:
    success , img = cam.read()

    imgRGB = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    #for single hand detection as well as drawing them.
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id , lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx , cy = int(lm.x*w) , int(lm.y*h)
                print(id , cx , cy)

                if id in [0,4,8,12,16,20]:
                    cv.circle(img , (cx,cy) , 10 , (0,0,0) , cv.FILLED) 
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    
    #fps calculation
    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time

    cv.putText(img , f'FPS : {int(fps)}' , (20,60) , cv.FONT_HERSHEY_COMPLEX , 1 , (0 , 0 , 0) , 3 )

    cv.imshow('Img' , img)
    if cv.waitKey(1) & 0xFF == ord('k'):
        break
