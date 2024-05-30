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


class handDetector():
    def __init__(self , mode=False , maxHands = 2 , detectionCon = 50 , trackCon = 50):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode , self.maxHands ,self.detectionCon , self.trackCon )
        self.mpDraw = mp.solutions.drawing_utils

    def findhands(self,img,draw=True):
        imgRGB = cv.cvtColor(img , cv.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

    #for single hand detection as well as drawing them.
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw :
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img
                # for id , lm in enumerate(handLms.landmark):
                #     h,w,c = img.shape
                #     cx , cy = int(lm.x*w) , int(lm.y*h)
                #     print(id , cx , cy)

                # if id in [0,4,8,12,16,20]:
                #     cv.circle(img , (cx,cy) , 15 , (255,0,0) , cv.FILLED) 
                #     self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
    
    # #fps calculation.
    # curr_time = time.time()
    # fps = 1/(curr_time - prev_time)
    # prev_time = curr_time
    
    # cv.putText(img , f"FPS:{int(fps)}", (10,70), cv.FONT_HERSHEY_COMPLEX , 1 , (0,255,0) , 1)

    # cv.imshow('Read',img)
    # #break off if the key K is pressed.
    # if cv.waitKey(1) & 0xFF == ord('k'):
    #     break

        
def main():
    prev_time = 0
    curr_time = 0
    vid_cap  = cv.VideoCapture(0) 
    detector = handDetector()
    while True:
        success , img  = vid_cap.read()
        img = detector.findhands(img)
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