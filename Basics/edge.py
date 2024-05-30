#edge detection.
import cv2 as cv
import numpy as np

img = cv.imread('photos_videos/skyline.jpg')
cv.imshow('Sky' , img)
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

# #Laplace method for edge detection.
# lap = cv.Laplacian(gray , cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian' , lap)

#Sobel (computes gradients in two directions.)
sobelx = cv.Sobel(gray , cv.CV_64F , 1 , 0)
sobely = cv.Sobel(gray , cv.CV_64F , 0 , 1)
cv.imshow('Sobel X' , sobelx)
cv.imshow('Sobel Y' , sobely)

#Canny edge detection.
canny = cv.Canny(gray , 150 , 175)
cv.imshow('Canny Edge' , canny)

cv.waitKey(0)
