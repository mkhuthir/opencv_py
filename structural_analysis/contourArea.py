#!/usr/bin/python3

import numpy as np
import cv2
import random

# load color image
img = cv2.imread("../img/fuzzy.png",1)
cv2.imshow("Original",img)

# Convert from BGR to HSV and apply GaussianBlur
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3),0)

# Apply inverse binary threshold
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
cv2.imshow("Binary",thresh)

# Find Contours
_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Number of found contours:", len(contours))

# Filter Contours based on its area
filtered = []
area_max = 1050

for c in contours:
	if cv2.contourArea(c) < area_max:
		continue
	filtered.append(c)

print("Number of filtered contours:", len(filtered))

# Draw filtered contours
objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')
for c in filtered:
	col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	cv2.drawContours(objects,[c], -1, col, -1)
	area = cv2.contourArea(c)
	p = cv2.arcLength(c,True)
	print("Area {0:8.2f} Perimeter {1:8.2f}".format(area,p))

# Show image
cv2.imshow("Contours",objects)

cv2.waitKey(0)
cv2.destroyAllWindows()