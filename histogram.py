import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photo/gargoyle.jpg')
[height,width] = img.shape[:2]

img = cv.resize(img, (int(width*0.4), int(height*0.4)), interpolation=cv.INTER_AREA)
cv.imshow('Gargoyle', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# histogram for grayscale
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
plt.title('Grayscale')
plt.xlabel('Bins')
plt.ylabel('Num of px')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# histogram for color
colors = ('b','g','r')

plt.figure()
plt.title('Color')
plt.xlabel('Bins')
plt.ylabel('Num of px')

for i,col in enumerate(colors):
    color_hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(color_hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)