#!/usr/bin/python3

import numpy as np
import cv2

# Define parameters
point1 = (0,0)
point2 = (511,511)
color = (255,0,0)
thickness = 3
lineType = cv2.LINE_AA

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw Line
cv2.line(img,point1,point2,color,thickness,lineType)

# Show image
cv2.imshow('Line',img)

# Wait for a key-press then destroy window and exit
cv2.waitKey(0)
cv2.destroyAllWindows()

