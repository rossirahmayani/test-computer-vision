import cv2 as cv
import numpy as np


# create blank img
blank = np.zeros((500,500, 3), dtype='uint8') # blank canvas img
width = blank.shape[1]
height = blank.shape[0]

cv.imshow('Blank', blank)


# paint img in color
blank[:] = 0,255,0 # green
cv.imshow('Green', blank)

blank[200:300, 200:300] = 255,0,0 # blue in x: 200-300, y: 200-300
cv.imshow('Blue', blank)


# draw rectangle
rectangle = cv.rectangle(blank, (0,0), (250,250), (0,0,0), thickness=2) # black rectangle
cv.imshow('Rectangle', rectangle)


# draw circle
circle = cv.circle(blank, (width//2, height//2), 30, (0,0,255), thickness=-1) # red circle
cv.imshow('Circle', circle)


# draw line
line = cv.line(blank, (0,0), (250,250), (0,0,0), thickness=2) # black line
cv.imshow('Line', line)


# write text
text = cv.putText(blank, 'Hoopla', (100,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (225,0,0), 2) # text
cv.imshow('Text', text)


cv.waitKey(0)