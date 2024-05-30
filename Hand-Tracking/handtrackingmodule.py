import cv2 as cv
import mediapipe as mp
import time

#to capture real time video.
vid_cap  = cv.VideoCapture(0)

#using mediapipe built-in hand detection models.
mpHands = mp.solutions.hands
hands = mpHands.Hands()
#to draw the lines on the hand detected.
mpDraw = mp.solutions.drawing_utils

prev_time = 0
curr_time = 0

while True:
    success , img  = vid_cap.read()
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
                    cv.circle(img , (cx,cy) , 15 , (255,0,0) , cv.FILLED) 
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    
    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time
    
    cv.putText(img , f"FPS:{int(fps)}", (10,70), cv.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , 1)

    cv.imshow('Read',img)
    #break off if the key K is pressed.
    if cv.waitKey(1) & 0xFF == ord('k'):
        break

def main():
    prev_time = 0
    curr_time = 0
    while True:
        success , img  = vid_cap.read()
        curr_time = time.time()
        fps = 1/(curr_time - prev_time)
        prev_time = curr_time
    
        cv.putText(img , f"FPS:{int(fps)}", (10,70), cv.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , 1)

        cv.imshow('Read',img)
        #break off if the key K is pressed.
        if cv.waitKey(1) & 0xFF == ord('k'):
            break



if __name__ == "__main__":
    main()
