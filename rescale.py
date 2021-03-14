import cv2 as cv 

# method rescale
def rescaleFrame(frame, scale=0.75): # for img, vid, live vid
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height): # only live video
    capture.set(3,width)
    capture.set(4,height)



img = cv.imread('photo/gargoyle.jpg')
img_new = rescaleFrame(img, 0.2)

cv.imshow('G', img)
cv.imshow('G_new', img_new)

cv.waitKey(0)

