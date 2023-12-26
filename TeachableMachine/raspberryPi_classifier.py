from teachable_machine_lite import TeachableMachineLite
import cv2 as cv

cap = cv.VideoCapture(0)

model_path = 'resources/rpi_model/model.tflite'
image_file_name = "frame.jpg"
labels_path = "resources/rpi_model/labels.txt"

tm_model = TeachableMachineLite(model_path=model_path, labels_file_path=labels_path)
c = 0
while True:
    ret, frame = cap.read()
    cv.imshow('Cam', frame)
    if c > 10:
        cv.imwrite(image_file_name, frame)
        results = tm_model.classify_frame(image_file_name)
        print(results["label"])
        c=0
    else:
        c+=1

    k = cv.waitKey(1)
    if k% 255 == 27:
        # press ESC to close camera view.
        break
