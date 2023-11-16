import cv2 as cv

imagePath = "resources/pal.jpg"
img = cv.imread(imagePath)

cv.rectangle(img, (300, 300), (390, 420), (255, 0, 0), thickness=3)

cv.imshow("Image with Rectangle", img)

cv.waitKey(0)
