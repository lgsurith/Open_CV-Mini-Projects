import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('photos_videos/skyline.jpg')
cv.imshow('img',img)

blank  = np.zeros(img.size[:2] , dtype='uint8')


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('gray' , gray)

#grayscale histogram
gray_hist = cv.calcHist([gray] , [0] , None , [256] , [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)
