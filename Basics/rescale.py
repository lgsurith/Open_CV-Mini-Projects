import cv2 as cv

#we must rescale or resize to lower res() / cv.waitkey()

#img = cv.imread('photos_video/image1.jpg')
#cv.imshow('Image1',img)

#rescaling
def rescaleframe(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('photos_videos/copy_1.mp4')
while True:
    isTrue , frame = capture.read()
    frame_resized = rescaleframe(frame)

    cv.imshow('Video',frame) 
    cv.imshow('Resize_Video',frame_resized) 

    if cv.waitKey(40) & 0xFF==ord('d'):  
        break

capture.release()
cv.destroyAllWindows()
#cv.waitKey(0)