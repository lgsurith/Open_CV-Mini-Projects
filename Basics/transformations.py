import cv2 as cv
import numpy as np

img = cv.imread('photos_videos/skyline.jpg')
cv.imshow('Image',img)

#translating the image 
# -x-->left
# -y -->up
# x --> right
# y --> down 

def translate(img , x , y):
    transMat = np.float32([[1,0,x] , [0,1,y]])
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , transMat , dimensions)

translated = translate(img , -100 , 100)
cv.imshow('Translate' , translated)

def rotate(img , angle , rotpoint = None):
    (height , width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width // 2 , height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotpoint , angle , 1.0)
    dimensions = (width , height)

    return cv.warpAffine(img , rotMat , dimensions)

#to rotate clockwise (include negative angle)
rotated = rotate(img , 45)
cv.imshow('Rotate' , rotated)

#flip
flip = cv.flip(img , -2)
cv.imshow('Flipped ', flip)


cv.waitKey(0)
# cv.destroyAllWindows()
