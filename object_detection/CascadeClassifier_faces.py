#!/usr/bin/python3

import numpy as np
import cv2

# Read faces image and convert from BGR to Gray
img = cv2.imread("../img/faces.jpeg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Load Haar cascade classifier file
path = "../xml/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(path)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
print(len(faces))

# Draw bounding boxes on detected faces
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

# Show image
cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()