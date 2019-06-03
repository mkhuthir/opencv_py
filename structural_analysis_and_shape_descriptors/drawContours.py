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
thickness = 1
color = (255, 0, 255)

# Create new blank image
objects = np.zeros([img.shape[0], img.shape[1],3], 'uint8')

# Find Area, Perimeter, Momoents, and Center of each Contour
count = 0
for c in contours:
	count += 1
	cv2.drawContours(objects, [c], -1, color, thickness)

	area = cv2.contourArea(c)
	perimeter = cv2.arcLength(c, True)

	M = cv2.moments(c)
	cx = int( M['m10']/M['m00'])
	cy = int( M['m01']/M['m00'])
	cv2.circle(objects, (cx,cy), 4, (0,0,255), -1)

	print("Contour:{0:4d} Area: {1:8.2f} perimeter: {2:8.2f}".format(count, area, perimeter))

# Show results
cv2.imshow("Contours",objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
