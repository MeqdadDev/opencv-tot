import cv2 as cv

imagePath = "resources/pal.jpg"
img = cv.imread(imagePath)

cv.imshow("Original", img)

cropped_image = cv.getRectSubPix(img, (300, 300), (390, 420))

cv.imshow("Cropped", cropped_image)
cv.waitKey(0)
