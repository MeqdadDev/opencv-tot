import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0) 

# Threshold of blue in HSV space 
lower_blue = np.array([60, 35, 140]) 
upper_blue = np.array([180, 255, 255]) 

while True: 
	_, frame = cap.read() 
	# It converts the BGR color space of image to HSV color space 
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) 
	
	# preparing the mask to overlay
	mask = cv.inRange(hsv, lower_blue, upper_blue)
	
	# The black region in the mask has the value of 0, 
	# so when multiplied with original image removes all non-blue regions 
	result = cv.bitwise_and(frame, frame, mask = mask) 

	cv.imshow('Frame', frame) 
	cv.imshow('Mask', mask) 
	cv.imshow('Result', result) 
	
	k = cv.waitKey(1)
	if k % 255 == 27:
		break

cv.destroyAllWindows() 
cap.release() 

