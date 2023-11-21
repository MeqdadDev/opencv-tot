import numpy as np
import cv2

# Define the size and dtype of the desired image
height, width = 680, 720
channels = 3

# Create a NumPy matrix as the image
image_mat = np.zeros((height, width, channels), dtype=np.uint8)

# Fill the image with required values based on RGB color space.
image_mat[:] = 0,255,0

# Display the image
cv2.imshow('Blank Image', image_mat)
cv2.waitKey(0)