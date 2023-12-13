import cv2 as cv

face_cascade = cv.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

# NOTE: Add the names as the same way that you wrote the name in Collection phase.
people = ['Meqdad', 'Person2', 'Person3']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('trained_model.yml')

def detect_face(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_rectangle = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    return faces_rectangle, gray

cap = cv.VideoCapture(0)

while True:
    camStream, frame = cap.read()

    rectangles, gray = detect_face(frame)

    for (x,y,w,h) in rectangles:
        roi = gray[y:y+h,x:x+w]

        label, confidence = face_recognizer.predict(roi)
        print(f'Person = {people[label]}, Confidence = {confidence}')

        cv.putText(frame, str(people[label]), (x,y-20), cv.FONT_ITALIC, 1.0, (0,255,0), thickness=2)
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Face', frame)
    k = cv.waitKey(1)
    if k % 256 == 27:
        print("ESC is pressed... Cancel")
        break
