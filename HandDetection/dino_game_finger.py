import cv2 as cv
from pynput.keyboard import Key, Controller
from detectors_world import DetectorCreator
from time import sleep

cap = cv.VideoCapture(0)

creator = DetectorCreator()

hand = creator.getDetector("hand")

keyboard = Controller()

def check_index_finger(landmarks):
    if len(landmarks) != 0:
        print(lms[4])
        if landmarks[8][2] < 150:
            print("UP")
            keyboard.press(Key.up)
            sleep(0.1)
            keyboard.release(Key.up)
        elif landmarks[8][2] > 350:
            print("DOWN")
            keyboard.press(Key.down)
            sleep(0.1)
            keyboard.release(Key.down)

while True:
    status, img = cap.read()
    hand.detect(img, drawOnHand=True)

    lms = hand.locate(img, drawOnHand=True, handsNumber=1)
    check_index_finger(lms)

    cv.line(img, (100, 150), (500, 150), (0, 255, 0), 1)
    cv.line(img, (100, 350), (500, 350), (0, 255, 0), 1)
    
    cv.imshow("T-Rex Dino Game", img)
    k = cv.waitKey(1)
    
    # if Esc is pressed -> Exit
    if k % 255 == 27:
        break