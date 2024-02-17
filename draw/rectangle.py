#!/usr/bin/python3

import numpy as np
import cv2

# Define parameters
point1 = (384,40)
point2 = (120,128)
color = (0,255,0)
thickness = 3

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw Rectangle
cv2.rectangle(img,point1,point2,color,thickness)

# Show image
cv2.imshow('Rectangle',img)

# Wait for a key-press then destroy window and exit
cv2.waitKey(0)
cv2.destroyAllWindows()

