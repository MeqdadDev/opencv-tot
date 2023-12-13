import cv2 as cv
cam = cv.VideoCapture(0)
eye_cascade = cv.CascadeClassifier('resources/haarcascade_eye.xml')

def detect_eyes(img):
    eyes_frame = img.copy()
    # Returns the rectangle borders
    eyes_rects = eye_cascade.detectMultiScale(eyes_frame)
    for (x, y, w, h) in eyes_rects:
        cv.rectangle(eyes_frame, (x, y), (x+w, y+h), (255, 0, 255), 5)
    return eyes_frame

while True:
    _, frame = cam.read()
    detection = detect_eyes(frame)
    cv.imshow('Eyes Detection View', detection)
    k = cv.waitKey(1)

    if k % 256 == 27:
        break

cam.release()
