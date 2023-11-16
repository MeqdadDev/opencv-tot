import cv2 as cv

imagePath = "resources/pal.jpg"
img = cv.imread(imagePath)

cv.imshow("Original", img)

resized_image = cv.resize(img, (300, 200))
cv.imshow("Resized", resized_image)

cv.waitKey(0)