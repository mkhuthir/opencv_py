#!/usr/bin/python3

import numpy as np
import cv2 as cv

# Load image in colors
img = cv.imread("../img/tomatoes.jpg",1)
cv.imshow("Original",img)

# Convert from BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Apply inverse binary threshold
res,thresh = cv.threshold(hsv[:,:,0], 25, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresh",thresh)

cv.waitKey(0)
cv.destroyAllWindows()