#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Load image and convert to gray
img = cv.imread("../_img/faces.jpeg",1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# load haae cascade file
path = "xml/haarcascade_eye.xml"
eye_cascade = cv.CascadeClassifier(path)

# Detect eyes
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.01,minNeighbors=10,minSize=(10,10))
print("Eyses detected:",len(eyes))

# Draw circles around detected eyes
for (x, y, w, h) in eyes:
	xc = (x + x+w)/2
	yc = (y + y+h)/2
	radius = w/2
	cv.circle(img, (int(xc),int(yc)), int(radius), (255,0,0), 2)

# Show result
cv.imshow("Eyes",img)

cv.waitKey(0)
cv.destroyAllWindows()