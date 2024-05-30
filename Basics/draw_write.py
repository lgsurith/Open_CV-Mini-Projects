import cv2 as cv
import numpy as np 

#to draw on blank images first.
#datatype uint8 is of image.

blank = np.zeros((500,500),dtype='uint8')
cv.imshow('Blank',blank)
img = cv.imread('photos_videos/image1.jpg')
cv.imshow('Image',img)

cv.waitKey(0)
