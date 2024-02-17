#!/usr/bin/python3

import numpy as np
import cv2 as cv

# Define parameters
center = (250,250)
radius = 63
color = (0,200,255)
thickness = -1

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw circle
cv.circle(img, center, radius, color, thickness)

# Show image
cv.imshow('Circle',img)

# Wait for a key-press then destroy window and exit
cv.waitKey(0)
cv.destroyAllWindows()

