#!/usr/bin/python3

import cv2
import numpy as np

# Define parameters
isClosed = True
color = (0,255,0)
points = np.array([ [110, 141], 
                    [106, 132],
                    [50,  250],
                    [150, 230],
                    [196, 188],
                    [158, 185]])

# Create a black image
img = np.zeros((300, 300, 3), dtype='uint8')


# Draw Polylines
cv2.polylines(img, [points], isClosed, color )

# Show image
cv2.imshow('Polylines',img)

# Wait for a key-press then destroy window and exit
cv2.waitKey(0)
cv2.destroyAllWindows()

