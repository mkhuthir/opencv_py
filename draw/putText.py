#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Define parameters
text = 'Hello OpenCV'
org = (10,128)
fontFace = cv.FONT_HERSHEY_SIMPLEX
fontScale = 1.5
color = (0,255,0)
thickness = 2
lineType = cv.LINE_AA


# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Add text
cv.putText(img,text,org, fontFace, fontScale,color,thickness,lineType)

# Show image
cv.imshow('Text',img)

# Wait for a key-press then destroy window and exit
cv.waitKey(0)
cv.destroyAllWindows()

