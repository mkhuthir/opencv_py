#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Load image in colors
img = cv.imread("../_img/tomatoes.jpg",1)
cv.imshow("Original",img)

# Apply Canny filter
edges = cv.Canny(img, 100, 70)
cv.imshow("Canny",edges)

cv.waitKey(0)
cv.destroyAllWindows()