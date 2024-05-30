import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('photos_videos/skyline.jpg')
cv.imshow('Test' , img)

rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

#THE OPENCV module reads the image as BGR.
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

#bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Hue' , hsv)

#bgr to lab
lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
cv.imshow('LED' , lab)


cv.waitKey(0)
