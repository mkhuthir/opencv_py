#!/usr/bin/python3

import numpy as np
import cv2 as cv

# Define parameters
center = (256,200)
axes = (100,50)
angle = 0
startAngle = 0
endAngle = 180
color = (0,0,255)
thickness = 2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw Ellipse
cv.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)

# Show image
cv.imshow('Ellipse',img)

# Wait for a key-press then destroy window and exit
cv.waitKey(0)
cv.destroyAllWindows()

