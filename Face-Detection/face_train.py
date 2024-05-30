import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Face-Detection/face2.jpeg')
# cv.imshow('Dune' , img)

#we must resize the image as we have a larger pixel value of an image.
#done by interpolation as well as resize.
down_width = 900
down_height = 1200
down_points = (down_width , down_height)
resized_down = cv.resize(img , down_points , interpolation = cv.INTER_LINEAR)

cv.imshow('Resized' , resized_down)

# convert image to grayscale for higher accuracy.
gray = cv.cvtColor(resized_down , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)


#we will be using pre trained Haar Cascade classifier to identify the faces.
haar_cascade = cv.CascadeClassifier('Face-Detection/haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(resized_down , scaleFactor=1.1 , minNeighbors=5)

#bounding box
for (x,y,w,h) in faces_rect:
    cv.rectangle(resized_down , (x,y) , (x+w , y+h) , (0,255,0) , thickness=2)

cv.imshow('Detected' , resized_down)

cv.waitKey(0)
