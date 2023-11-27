import cv2 as cv
import numpy as np

# Create a sample binary image (white square on a black background)
image = np.zeros((300, 300), dtype=np.uint8)
image[100:200, 100:200] = 255  # Creating a white square

# Define the structuring element/kernel (here a 5x5 rectangular kernel)
kernel = np.ones((5, 5), np.uint8)

# Perform erosion on the binary image using the defined kernel
eroded_image = cv.erode(image, kernel, iterations=1)

cv.imshow('Original Binary Image', image)
cv.imshow('Eroded Binary Image', eroded_image)

cv.waitKey(0)
cv.destroyAllWindows()
