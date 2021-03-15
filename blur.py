import cv2 as cv

img = cv.imread('photo/gargoyle.jpg')
[height,width] = img.shape[:2]

img = cv.resize(img, (int(width*0.4), int(height*0.4)), interpolation=cv.INTER_AREA)
cv.imshow('Gargoyle', img)

avg = cv.blur(img, (5,5))
cv.imshow('Average', avg)

gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('Gauss', gauss)

med = cv.medianBlur(img, 5)
cv.imshow('Median', med)

bil = cv.bilateralFilter(img, 5, 30, 25)
cv.imshow('Bilateral', bil)


cv.waitKey(0)