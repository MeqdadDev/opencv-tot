import cv2 as cv
import pytesseract

def get_ocr(img):
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)

img = cv.imread("resources/ocr_text.png")

cv.imshow('OCR Result', img)
text_ocr = get_ocr(img)
print(text_ocr)
cv.waitKey(0)
