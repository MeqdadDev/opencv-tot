import cv2 as cv

img = cv.imread("resources/pal.jpg")
cv.imshow("Original", img)

flip_h = cv.flip(img, 1)
cv.imshow("Horizontal Flip", flip_h)

flip_v = cv.flip(img, 0)
cv.imshow("Vertical Flip", flip_v)

flip_vh = cv.flip(img, -1)
cv.imshow("Vertical + Horizontal Flip", flip_vh)

cv.waitKey(0)
cv.destroyAllWindows()
