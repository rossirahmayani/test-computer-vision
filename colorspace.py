import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photo/animals.jpg')
[height,width] = img.shape[:2]
img = cv.resize(img, (int(width*0.4), int(height*0.4)), interpolation=cv.INTER_AREA)
cv.imshow('Animal', img)

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# matplot lib view (RGB)
plt.imshow(img)
plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()


cv.waitKey(0)