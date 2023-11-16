import cv2 as cv

imagePath = "resources/pal.jpg"
img = cv.imread(imagePath)

cv.circle(img, center=(300, 278), radius=50, color=(0, 0, 255), thickness=2)

cv.imshow("Image with Circle", img)

cv.waitKey(0)
