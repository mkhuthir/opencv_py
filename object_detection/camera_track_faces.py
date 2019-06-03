#!/usr/bin/python3

import numpy as np
import cv2

# Start Capture
cap = cv2.VideoCapture(0)

# Load Haar cascade classifier file
path = "../xml/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(path)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
    
    # Draw bounding boxes on detected faces
    for (x, y, w, h) in faces:
	    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # Exit if ESC key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()