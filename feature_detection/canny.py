#!/usr/bin/python3

import numpy as np
import cv2

# Load image in colors
img = cv2.imread("../img/tomatoes.jpg",1)
cv2.imshow("Original",img)

# Apply Canny filter
edges = cv2.Canny(img, 100, 70)
cv2.imshow("Canny",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()