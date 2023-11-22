import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0) 

# Threshold of blue in HSV space 
lower_blue = np.array([60, 35, 140]) 
upper_blue = np.array([180, 255, 255]) 

while True: 
	_, frame = cap.read() 

	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
	
	mask = cv.inRange(hsv, lower_blue, upper_blue)
	
	result = cv.bitwise_and(frame, frame, mask = mask) 

	cv.imshow('Frame', frame) 
	cv.imshow('Mask', mask) 
	cv.imshow('Result', result) 
	
	k = cv.waitKey(1)
	if k % 255 == 27:
		break

cv.destroyAllWindows() 
cap.release() 

