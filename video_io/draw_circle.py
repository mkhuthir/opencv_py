#!/usr/bin/python3

import cv2

# Start Capture
cap = cv2.VideoCapture(0)

# Circle paramaters
color = (0,255,0)
line_width = 3
radius = 100
point = (0,0)

# Define call back function
def click(event, x, y, flags, param):
	global point
	if event == cv2.EVENT_LBUTTONDOWN:
		print("Pressed",x,y)
		point = (x,y)

# Set the call back function for the window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)

# Main loop
while(True):
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv2.circle(frame, point, radius, color, line_width)
	cv2.imshow("Frame",frame)
 
	if cv2.waitKey(1) & 0xFF == 27:
		break

# Stop capture and destroy window
cap.release()
cv2.destroyAllWindows()
