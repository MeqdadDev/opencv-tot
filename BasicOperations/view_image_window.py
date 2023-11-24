import cv2 as cv

img1 = cv.imread("resources/pal.jpg")
window_palestine = "Palestine Flag"
cv.namedWindow(window_palestine, cv.WINDOW_AUTOSIZE)
cv.imshow(window_palestine, img1)
cv.waitKey(0)
cv.destroyWindow(window_palestine)

img2 = cv.imread("resources/purpose.jpg")
window_purpose = "Purpose Logo"
cv.namedWindow(window_purpose, cv.WINDOW_NORMAL)
cv.imshow(window_purpose, img2)
cv.waitKey(0)
cv.destroyWindow(window_purpose)
