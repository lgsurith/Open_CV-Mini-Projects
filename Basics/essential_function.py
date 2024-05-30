import cv2 as cv

img = cv.imread('photos_videos\skyline.jpg')
cv.imshow('Test',img)

#Grayscale conversion.
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

#blurring the image (reducing the noise).[gaussian blur]
#kernel size must be an odd number.
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#canny edge detection.
canny = cv.Canny(blur,125,175)
cv.imshow('Canny images',canny)

#dilating the images
dilated = cv.dilate(canny , (3,3) , iterations = 5)
cv.imshow('Dilated' , dilated)

#eroding of image
erode = cv.erode(dilated , (3,3) , iterations = 3)
cv.imshow('Erode' , erode) 

#Resize  [pass the image --> to the pixel size]
resize = cv.resize(img , (360,360) , interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resize)

#crop
cropped = img[50:100 , 200:400]
cv.imshow('Cropped' , cropped)

cv.waitKey(0)
cv.destroyAllWindows()

