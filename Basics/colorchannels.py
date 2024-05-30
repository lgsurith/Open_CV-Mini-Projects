import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

img = cv.imread('photos_videos/skyline.jpg')
cv.imshow('Sky' , img)
blank = np.zeros(img.shape[:2] , dtype ='uint8')  #for initiating a blank screen.

#opencv processes it as BGR so split images into bgr.
b,g,r = cv.split(img)

#just depicts the blue ,red and green seperated.
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

merged = cv.merge([b,g,r])
cv.imshow('Merged' , merged)

cv.waitKey(0)
