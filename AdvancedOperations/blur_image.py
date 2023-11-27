import cv2 as cv

imagePath = "resources/pal.jpg"

img = cv.imread(imagePath)

# Blur the image using average kernel
blur_avg = cv.blur(img, (7, 7))

# Blur the image using Gaussian kernel
blur_gaussian = cv.GaussianBlur(img, (7, 7), 0)

cv.imshow('Original', img)
cv.imshow('Average Blur', blur_avg)
cv.imshow('Gaussian Blur', blur_gaussian)
cv.waitKey(0)
cv.destroyAllWindows()