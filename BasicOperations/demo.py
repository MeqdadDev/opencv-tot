import cv2 as cv

img = cv.imread("resources/pal.jpg", cv.IMREAD_COLOR)

# print(img)
# print("Data type of this image::: ", img.dtype)
# cv.imshow("BGR", img)

# rgb_image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# gray_image = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# resized_image = cv.resize(img, (300, 200))
# cropped_image = cv.getRectSubPix(img, (300, 300), (390, 420))

# cv.rectangle(img, (300, 300), (390, 420), (0, 255, 0), 2)

# cv.imshow("RGB", rgb_image)
# cv.imshow("Gray", gray_image)
# cv.imshow("Resized", resized_image)
# cv.imshow("Cropped", cropped_image)

# cv.imwrite("new_image.png", img)
cv.imshow("Original", img)
cv.waitKey(0)
