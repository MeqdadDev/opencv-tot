import cv2 as cv

imagePath = "resources/pal.jpg"
img = cv.imread(imagePath)

cv.putText(img, "Meqdad", (100, 100), 
           cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

cv.imshow("Image with Text", img)

cv.waitKey(0)
