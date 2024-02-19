#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024


import numpy as np
import cv2 as cv

# Define parameters
point1 = (0,0)
point2 = (511,511)
color = (255,0,0)
thickness = 3
lineType = cv.LINE_AA

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw Line
cv.line(img,point1,point2,color,thickness,lineType)

# Show image
cv.imshow('Line',img)

# Wait for a key-press then destroy window and exit
cv.waitKey(0)
cv.destroyAllWindows()

