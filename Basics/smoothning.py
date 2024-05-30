import cv2 as cv
#BASICALLY THIS MODULE EXPLAINS WHICH TYPE OF BLUR IS BETTER.

img = cv.imread('photos_videos\skyline.jpg')
cv.imshow('Test',img)

#blurring by the methof of kernels.
#averaging has more blur effect than the gaussian blur.

average = cv.blur(img , (7,7))  #normal blur pass the image as well as res size per pixel.
cv.imshow('Average Blur' , average)

gauss = cv.GaussianBlur(img , (7,7) , 0)
cv.imshow('Gauss' , gauss)

#bilateral blur
bi = cv.bilateralFilter(img , 5 , 15 , 15)
cv.imshow('bilateral' , bi)

cv.waitKey(0)
