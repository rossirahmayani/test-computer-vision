import cv2 as cv
import numpy as np

img = cv.imread('photo/animals.jpg')

[height,width] = img.shape[:2]
img = cv.resize(img, (int(width*0.4), int(height*0.4)), interpolation=cv.INTER_AREA)
cv.imshow('Animal', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


# split channel
b,g,r = cv.split(img)

cv.imshow('B', b)
cv.imshow('G', g)
cv.imshow('R', r)

print(f'Image : {img.shape}')
print(f'Blue  : {b.shape}')
print(f'Green : {g.shape}')
print(f'Red   : {r.shape}')

# merge channel
merge = cv.merge([b,g,r])
cv.imshow('Merge', merge)

# reconstruct color
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)