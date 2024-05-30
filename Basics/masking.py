import cv2 as cv
import numpy as np

#using the bitwise we can perform masking.

img = cv.imread('photos_videos/skyline.jpg')
cv.imshow('una',img)

#for creating blank gui image.
blank = np.zeros(img.shape[:2] , dtype = 'uint8')
cv.imshow('blank' , blank)

mask = cv.circle(blank , (img.shape[1] //2 , img.shape[0]//2) , 100 , 255 , -1 )
cv.imshow('mask',mask)

#size , pixel size , colour , thickeness.
masked = cv.bitwise_and(img , img , mask = mask)
cv.imshow('Mask' , masked)

cv.waitKey(0)
