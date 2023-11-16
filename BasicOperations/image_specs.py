import cv2 as cv

imagePath = "resources/pal.jpg"
img = cv.imread(imagePath)

print("Data type of this image::: ", img.dtype)
print("Dimensions of this image:::", img.shape)
