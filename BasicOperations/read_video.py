import cv2 as cv

videoPath = "resources/10sec.mp4"
cap = cv.VideoCapture(videoPath)

while True:
    ret, frame = cap.read()
    cv.imshow("Video", frame)
    k = cv.waitKey(22)
    # To check if ESC is pressed
    if k % 255 == 27:
        break

cap.release()
cv.destroyAllWindows()
