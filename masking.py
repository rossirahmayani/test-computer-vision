import cv2 as cv
import numpy as np

img = cv.imread('photo/gargoyle.jpg')
[height,width] = img.shape[:2]

img = cv.resize(img, (int(width*0.4), int(height*0.4)), interpolation=cv.INTER_AREA)
cv.imshow('Gargoyle', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2 -30, img.shape[0]//2 - 30), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)