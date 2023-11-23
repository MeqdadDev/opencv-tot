from detectors_world import DetectorCreator
import cv2 as cv

cap = cv.VideoCapture(0)

creator = DetectorCreator()
hand = creator.getDetector("hand")

while True:
    status, img = cap.read()
    hand.detect(img, drawOnHand=True)
    landmarks = hand.locate(img)
    print(landmarks)
    cv.imshow("Hand Detection", img)
    k = cv.waitKey(1)
    if k % 255 == 27:
        break

# Tracking a specific hand point:
# print(landmarks[8][1])
