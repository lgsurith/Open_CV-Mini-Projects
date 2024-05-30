import cv2 as cv

img=cv.imread('photos_videos/skyline.jpg')
cv.imshow('Sky' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

#switches the pixel image to that and then beyond.
threshold , thresh = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY)
cv.imshow('Thresh' , thresh)

threshold , thresh_inv = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY_INV)
cv.imshow('Thresh Inv' , thresh_inv)
#to perform threshold we must grayscale the image first.
#simple thresholding.


#adaptive threshold. (custom threshold value / find the optimal threshold value)
#the last parameter is used to find the kernel.
adaptive_thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY, 11 , 3)
cv.imshow('Adaptive Threshold' , adaptive_thresh)

cv.waitKey(0)
