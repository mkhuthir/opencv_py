#!/usr/bin/python3

import numpy as np
import cv2 as cv

# Read image in color
img = cv.imread('../img/detect_blob.png',1)

# Convert to Gray
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

# Apply Binary Threshold
thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
cv.imshow("Binary", thresh)

# Find Contours
_, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# Deep Copy the original image
img2 = img.copy()

# Draw Contours on copy
index = -1
thickness = 4
color = (255, 0, 255)

cv.drawContours(img2, contours, index, color, thickness)
cv.imshow("Contours",img2)

# Wait for a key press to exit
cv.waitKey(0)
cv.destroyAllWindows()
