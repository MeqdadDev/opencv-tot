import cv2 as cv

imagePath = "resources/pal.jpg"
img = cv.imread(imagePath)

cv.line(img, (100, 100), (200, 200), (0, 255, 0), thickness=2)
cv.imshow("Image with Line", img)

cv.waitKey(0)