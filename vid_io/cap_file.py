#!/usr/bin/python3

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('../vid/test.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame',gray)

    # Exit if ESC key is pressed
    if cv.waitKey(20) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()