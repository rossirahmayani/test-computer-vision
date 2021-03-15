import cv2 as cv 
import numpy as np

img = cv.imread('photo/gargoyle.jpg')
[height,width] = img.shape[:2]

# translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translate = translate(img,100,100)
cv.imshow('Translate', translate)


# rotation
def rotate(img, angle, point=None):
    [h,w] = img.shape[:2]

    if point is None:
        point = (w//2, h//2)
    
    rotMat = cv.getRotationMatrix2D(point, angle, 1.0)
    dimensions = (w,h)
    return cv.warpAffine(img, rotMat, dimensions)

rotate = rotate(img, 45)
cv.imshow('Rotate', rotate)


# resizing
resize = cv.resize(img, (int(width*0.2), int(height*0.2)), interpolation=cv.INTER_AREA)
cv.imshow('Resize', resize)


# flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)


# cropping
crop = img[200:400, 300:400]
cv.imshow('Crop', crop)


cv.waitKey(0)