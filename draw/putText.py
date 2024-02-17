#!/usr/bin/python3

import numpy as np
import cv2

# Define parameters
text = 'Hello OpenCV'
org = (10,128)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1.5
color = (0,255,0)
thickness = 2
lineType = cv2.LINE_AA


# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Add text
cv2.putText(img,text,org, fontFace, fontScale,color,thickness,lineType)

# Show image
cv2.imshow('Text',img)

# Wait for a key-press then destroy window and exit
cv2.waitKey(0)
cv2.destroyAllWindows()

