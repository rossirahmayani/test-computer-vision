import cv2 as cv 

# read image
img = cv.imread('photo/Yellow.png')
cv.imshow('Yellow', img)
cv.waitKey(0)


# read video
# capture = cv.VideoCapture(0) # reference to webcam
capture = cv.VideoCapture('video/wadesta.MP4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Wadesta', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows
