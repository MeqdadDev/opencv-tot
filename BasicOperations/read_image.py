import cv2 as cv

imagePath = "resources/pal.jpg"
img = cv.imread(imagePath)

# Matrix representation of image
print(img)

cv.imshow("Image View Window", img)

# Still visible and close if any key is pressed
cv.waitKey(0)