#!/usr/bin/python3

import numpy as np
import cv2

# Read image in color
img = cv2.imread('../img/detect_blob.png',1)

# Convert to Gray
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Apply Binary Threshold
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Binary", thresh)

# Find Contours
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Deep Copy the original image
img2 = img.copy()

# Draw Contours on copy
index = -1
thickness = 4
color = (255, 0, 255)

cv2.drawContours(img2, contours, index, color, thickness)
cv2.imshow("Contours",img2)

# Wait for a key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
