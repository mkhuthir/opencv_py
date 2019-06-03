#!/usr/bin/python3

import numpy as np
import cv2

# Load image in colors
img = cv2.imread("../img/tomatoes.jpg",1)
cv2.imshow("Original",img)

# Convert from BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Apply inverse binary threshold
res,thresh = cv2.threshold(hsv[:,:,0], 25, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()