#!/usr/bin/python3

import numpy as np
import cv2

# Load image and convert to gray
img = cv2.imread("../img/faces.jpeg",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# load haae cascade file
path = "../xml/haarcascade_eye.xml"
eye_cascade = cv2.CascadeClassifier(path)

# Detect eyes
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.01,minNeighbors=10,minSize=(10,10))
print("Eyses detected:",len(eyes))

# Draw circles around detected eyes
for (x, y, w, h) in eyes:
	xc = (x + x+w)/2
	yc = (y + y+h)/2
	radius = w/2
	cv2.circle(img, (int(xc),int(yc)), int(radius), (255,0,0), 2)

# Show result
cv2.imshow("Eyes",img)

cv2.waitKey(0)
cv2.destroyAllWindows()