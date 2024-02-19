#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import cv2 as cv
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
cv.polylines(img, [points], isClosed, color )

# Show image
cv.imshow('Polylines',img)

# Wait for a key-press then destroy window and exit
cv.waitKey(0)
cv.destroyAllWindows()

