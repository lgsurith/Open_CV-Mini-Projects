import cv2 as cv
import numpy as np

img = cv.imread('photos_videos/skyline.jpg')
cv.imshow('Test',img)

#to create a blank screen as hexcode 0 is for black.
blank = np.zeros(img.shape , dtype = 'uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

blur = cv.GaussianBlur(img , (7,7) , cv.BORDER_DEFAULT)
cv.imshow('Blurred' , blur)

#grab the edges using the canny edge detector
canny = cv.Canny(blur , 125 , 175)
cv.imshow('Cannied' , canny)

#heirarch - based on the img struct
#RETR_TREE --> Heir content
#RETR_EXTERNAL --> External Contours.

# to binarise the image we can use threshod >125 -> 0 and greater tham 255> 1.
ret , thresh = cv.threshold(gray , 125 , 255 , cv.THRESH_BINARY)
cv.imshow('Thresh' , thresh)

contours , hierarchies = cv.findContours(thresh, cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour found')

cv.drawContours(blank , contours , -1 , (0,0,255) , 2)
cv.imshow('Contour' , blank)


cv.waitKey(0)
