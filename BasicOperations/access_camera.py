import cv2 as cv

cap = cv.VideoCapture(0)

accessible, frame = cap.read()

window_name = "Camera Stream"
cv.namedWindow(window_name, cv.WINDOW_NORMAL)

while accessible:
    cv.imshow(window_name, frame)
    accessible, frame = cap.read()
    k = cv.waitKey(1)
    if not accessible or k == ord("q"): # Kill window when 'q' is pressed
        break
        
cap.release()
cv.destroyWindow(window_name)