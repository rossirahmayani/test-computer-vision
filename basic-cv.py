import cv2 as cv


img = cv.imread('photo/yellow.png')


# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# dilating
dilate = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilate)

# eroding
erode = cv.erode(dilate, (7,7), iterations=3)
cv.imshow('Eroded', erode)

# resize
resize = cv.resize(img, (200, 200), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resize)

# crop
crop = img[50:200, 50:100]
cv.imshow('Cropped', crop)

cv.waitKey(0)