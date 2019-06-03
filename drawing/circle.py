#!/usr/bin/python3

import numpy as np
import cv2

# Define parameters
center = (250,250)
radius = 63
color = (0,200,255)
thickness = -1

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw circle
cv2.circle(img, center, radius, color, thickness)

# Show image
cv2.imshow('Circle',img)

# Wait for a key-press then destroy window and exit
cv2.waitKey(0)
cv2.destroyAllWindows()

