#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import cv2 as cv

# Start Capture
cap = cv.VideoCapture(0)

# Circle paramaters
color = (0,255,0)
line_width = 3
radius = 100
point = (0,0)

# Define call back function
def click(event, x, y, flags, param):
	global point
	if event == cv.EVENT_LBUTTONDOWN:
		print("Pressed",x,y)
		point = (x,y)

# Set the call back function for the window
cv.namedWindow("Frame")
cv.setMouseCallback("Frame",click)

# Main loop
while(True):
	ret, frame = cap.read()

	frame = cv.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv.circle(frame, point, radius, color, line_width)
	cv.imshow("Frame",frame)
 
	if cv.waitKey(1) & 0xFF == 27:
		break

# Stop capture and destroy window
cap.release()
cv.destroyAllWindows()
