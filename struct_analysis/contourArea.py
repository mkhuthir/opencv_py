#!/usr/bin/python3

import numpy as np
import cv2 as cv
import random

# load color image
img = cv.imread("../img/fuzzy.png",1)
cv.imshow("Original",img)

# Convert from BGR to HSV and apply GaussianBlur
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3,3),0)

# Apply inverse binary threshold
thresh = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 205, 1)
cv.imshow("Binary",thresh)

# Find Contours
_, contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print("Number of found contours:", len(contours))

# Filter Contours based on its area
filtered = []
area_max = 1050

for c in contours:
	if cv.contourArea(c) < area_max:
		continue
	filtered.append(c)

print("Number of filtered contours:", len(filtered))

# Draw filtered contours
objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')
for c in filtered:
	col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	cv.drawContours(objects,[c], -1, col, -1)
	area = cv.contourArea(c)
	p = cv.arcLength(c,True)
	print("Area {0:8.2f} Perimeter {1:8.2f}".format(area,p))

# Show image
cv.imshow("Contours",objects)

cv.waitKey(0)
cv.destroyAllWindows()