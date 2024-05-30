import cv2 as cv
import mediapipe as mp
import time

#importing time to alter the framerate.

#using the mediapipe libraries to identify the pose.
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw  = mp.solutions.drawing_utils

#in-case if th evid turns out ot be huge resize it to identify the correct points from the pose image.
# down_width = 900
# down_height = 1200
# down_points = (down_width , down_height)

vid_cap = cv.VideoCapture("Advanced/Pose-Estimation/vid1.mp4")
prev_time = 0

while True:
    success , img = vid_cap.read()
    imgRGB = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    # resized_down = cv.resize(img , down_points , interpolation = cv.INTER_LINEAR)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img , results.pose_landmarks , mpPose.POSE_CONNECTIONS)
        for id , lm in enumerate(results.pose_landmarks.landmark):
            h , w , c = img.shape
            cx , cy = int(lm.x*w) , int(lm.y * h)
            cv.circle(img, (cx,cy) , 7 , (255,0,0) , cv.FILLED)


    cv.imshow("Image" , img)

    #standard code for fps.
    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time
    cv.putText(img , f"FPS:{int(fps)}", (70,50), cv.FONT_HERSHEY_COMPLEX , 3 , (255,0,0) , 3)

    if cv.waitKey(1) & 0xFF == ord('k'):
        break
