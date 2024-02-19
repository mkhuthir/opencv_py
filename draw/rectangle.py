#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Define parameters
point1 = (384,40)
point2 = (120,128)
color = (0,255,0)
thickness = 3

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw Rectangle
cv.rectangle(img,point1,point2,color,thickness)

# Show image
cv.imshow('Rectangle',img)

# Wait for a key-press then destroy window and exit
cv.waitKey(0)
cv.destroyAllWindows()

