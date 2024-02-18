#!/usr/bin/python3

import numpy as np
import cv2 as cv

# Read image in color
img = cv.imread('../_img/detect_blob.png',1)

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
thickness = 1
color = (255, 0, 255)

# Create new blank image
objects = np.zeros([img.shape[0], img.shape[1],3], 'uint8')

# Find Area, Perimeter, Momoents, and Center of each Contour
count = 0
for c in contours:
	count += 1
	cv.drawContours(objects, [c], -1, color, thickness)

	area = cv.contourArea(c)
	perimeter = cv.arcLength(c, True)

	M = cv.moments(c)
	cx = int( M['m10']/M['m00'])
	cy = int( M['m01']/M['m00'])
	cv.circle(objects, (cx,cy), 4, (0,0,255), -1)

	print("Contour:{0:4d} Area: {1:8.2f} perimeter: {2:8.2f}".format(count, area, perimeter))

# Show results
cv.imshow("Contours",objects)

cv.waitKey(0)
cv.destroyAllWindows()
