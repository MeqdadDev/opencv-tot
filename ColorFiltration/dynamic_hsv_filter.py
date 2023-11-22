import cv2 as cv
import numpy as np

def ignored(x):
    pass

cv.namedWindow('Trackbar')
cv.createTrackbar('H', 'Trackbar', 0, 179, ignored)
cv.createTrackbar('S', 'Trackbar', 0, 255, ignored)
cv.createTrackbar('V', 'Trackbar', 0, 255, ignored)

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Convert from BGR to HSV color space
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Get the current trackbar positions
    h = cv.getTrackbarPos('H', 'Trackbar')
    s = cv.getTrackbarPos('S', 'Trackbar')
    v = cv.getTrackbarPos('V', 'Trackbar')

    lower_range = np.array([h - 10, s, v])
    upper_range = np.array([h + 10, 255, 255])

    mask = cv.inRange(hsv, lower_range, upper_range)

    filtered_image = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('Original View', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Filtered Image', filtered_image)

    # Exit if 'Esc' key is pressed
    k = cv.waitKey(1)
    if k % 255 == 27:
        break

cap.release()
cv.destroyAllWindows()
