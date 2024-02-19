#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024


import numpy as np
import cv2 as cv

# Define parameters
point1 = (100,20)
point2 = (250,250)
color = (255,0,0)
thickness = 3
lineType = cv.LINE_AA
shift = 0
tipLength = 0.1

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw Arrow Line
cv.arrowedLine(img,point1,point2,color,thickness,lineType,shift,tipLength)

# Show image
cv.imshow('Line',img)

# Wait for a key-press then destroy window and exit
cv.waitKey(0)
cv.destroyAllWindows()

