import cv2 as cv
import numpy as np

img = cv.imread('photo/gargoyle.jpg')
[height,width] = img.shape[:2]

img = cv.resize(img, (int(width*0.4), int(height*0.4)), interpolation=cv.INTER_AREA)
cv.imshow('Gargoyle', img)

# draw canvas
blank = np.zeros(img.shape, dtype='uint8')

# turn grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', gray)

# blur
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# canny
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny', canny)

# threshold
ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'Found {len(contours)} contours in canny')

# draw contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'Found {len(contours)} contours in thresh')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('Contours Thresh', blank)

cv.waitKey(0)