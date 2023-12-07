from teachable_machine import TeachableMachine
import cv2 as cv
cap = cv.VideoCapture(0)
model = TeachableMachine(model_path="resources/tm_model/keras_model.h5",
                         labels_file_path="resources/tm_model/labels.txt")

image_path = "screenshot.jpg"

while True:
    _, img = cap.read()
    cv.imwrite(image_path, img)
    result = model.classify_image(image_path)
    print("class_index", result["class_index"])
    print("class_name:::", result["class_name"])
    print("class_confidence:", result["class_confidence"])
    cv.imshow("Video Stream", img)
    k = cv.waitKey(1)
    # To check if ESC is pressed
    if k % 255 == 27:
        break
