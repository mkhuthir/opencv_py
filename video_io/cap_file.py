#!/usr/bin/python3

import numpy as np
import cv2

cap = cv2.VideoCapture('../vid/test.avi')

while(cap.isOpened()):
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    # Exit if ESC key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()