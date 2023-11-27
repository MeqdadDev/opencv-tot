import cv2 as cv

imagePath = "resources/pal.jpg"

img = cv.imread(imagePath)

# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply Laplacian operator
laplacian = cv.Laplacian(gray, cv.CV_64F)

# Apply Canny operator
canny = cv.Canny(gray, 100, 200)

# Display the original and edge-detected images
cv.imshow('Original Image', img)
cv.imshow('Laplacian Edge Detection', laplacian)
cv.imshow('Canny Edge Detection', canny)

cv.waitKey(0)
cv.destroyAllWindows()