#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
radius = 3
color = (0,255,0)
thickness = -1
pressed = False

# click callback
def click(event, x, y, flags, param):
	global canvas, pressed
	if event == cv.EVENT_LBUTTONDOWN:
		pressed = True
		cv.circle(canvas,(x,y),radius,color,thickness)
	elif event == cv.EVENT_MOUSEMOVE and pressed == True:
		cv.circle(canvas,(x,y),radius,color,thickness)
	elif event == cv.EVENT_LBUTTONUP:
		pressed = False

# window initialization and callback assignment
cv.namedWindow("canvas")
cv.setMouseCallback("canvas", click)

# Forever draw loop
while True:

	cv.imshow("canvas",canvas)

	# key capture every 1ms
	ch = cv.waitKey(1)
	# if 'q' then quit the program
	if ch & 0xFF == ord('q'):
		break
	# if 'b' then change color to blue
	elif ch & 0xFF == ord('b'):
		color = (255,0,0)
	# if 'g' then change color to green
	elif ch & 0xFF == ord('g'):
		color = (0,255,0)
	# if 'r' then change color to red
	elif ch & 0xFF == ord('r'):
		color = (0,0,255)
	
	

cv.destroyAllWindows()