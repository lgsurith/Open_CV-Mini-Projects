import cv2 as cv

#reading images.
#img = cv.imread('photos_videos/image1.jpg')

#cv.imshow('Example',img)

#reading videos by frame.
capture = cv.VideoCapture('photos_videos/copy_1.mp4')

#we must use a while loop to run it and read it by frame by frame.

while True:
    isTrue , frame = capture.read()
    cv.imshow('Video',frame) #displays frame.

    if cv.waitKey(20) & 0xFF==ord('d'):  
        break

capture.release()
cv.destroyAllWindows()


