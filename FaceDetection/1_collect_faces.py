'''
Example: Collecting images for face detection.
By: Meqdad Darwish

###################################

Notes before you start:
1- Code will ask you about your name.
2- After running the code, you'll notice that some directories are created such as: 'CollectedFaces'.
3- You can find your images in the directory with your name in 'CollectedFaces' directory.
4- Press Space button to capture the image, and ESC button to close the camera.
5- Repeat these steps for each person to be recognised in the system.
'''

import cv2 as cv
import os

# To get the file's path
current_path = os.getcwd()

new_path = os.path.join(current_path, "CollectedFaces")

try:
    os.mkdir(new_path)
except FileExistsError:
    print("CollectedFaces is already created...")

# Your name here....
name = input("Enter your name to be recognized: ")

full_path = os.path.join(new_path, name)

try:
    os.mkdir(full_path)
except FileExistsError:
    print(f"{name} directory is already created... Previous images will be deleted.")

cam = cv.VideoCapture(0)

img_counter = 1

while True:
    is_success, frame = cam.read()
    if not is_success:
        print("failed to capture image.")
        break
    cv.imshow("Collecting Data Phase | Press space to capture", frame)

    # Stores the pressed key by the user.
    k = cv.waitKey(1)

    # Check if ESC is pressed
    if k % 256 == 27:
        print("ESC is pressed... Cancel")
        break

    # Check if space is pressed
    elif k % 256 == 32:
        img_name = f"{full_path}/{name}_img_{img_counter}.jpg"
        cv.imwrite(img_name, frame)
        print(img_name)
        print(f"Image #{img_counter} saved!")
        img_counter += 1

cam.release()
cv.destroyAllWindows()
