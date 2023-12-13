import os
import cv2 as cv
import numpy as np

# NOTE: Add the names as the same way that you wrote the name in Collection phase.
people = ["Meqdad", "Person2", "Person3"]

current_path = os.getcwd()

DIR = os.path.join(current_path, "CollectedFaces")

face_cascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

features = []
labels = []

print("********************************")
print("Model training started")
print("********************************")

for person in people:
    path = os.path.join(DIR, person)
    label = people.index(person)
    imgNum = 1
    for img in os.listdir(path):
        img_path = os.path.join(path,img)

        img_array = cv.imread(img_path)
        if img_array is None:
            continue

        print(f"Training for {person}, image #{imgNum}")
            
        gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

        faces_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

        for (x,y,w,h) in faces_rect:
            faces_roi = gray[y:y+h, x:x+w]
            features.append(faces_roi)
            labels.append(label)
        imgNum+=1

print("********************************")
print("Model training finished")

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save("trained_model.yml")

np.save("features.npy", features)
np.save("labels.npy", labels)

print("********************************")
print("Trained model saved successfully")
