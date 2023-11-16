import cv2 as cv

img = cv.imread("resources/pal.jpg")

rgb_image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb_image)

gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray_image)

hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv_image)

cv.waitKey(0)
