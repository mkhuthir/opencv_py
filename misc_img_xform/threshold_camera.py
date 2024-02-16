#!/usr/bin/python3

import numpy as np
import cv2

# Threshold values to be used
thresh_min = 85
thresh_max = 255

# Start Capture
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert from BGR to Gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Do Binary threshold cv2 function (fast process)
    ret, bin_img = cv2.threshold(gray, thresh_min, thresh_max, cv2.THRESH_BINARY)

    # Display the resulting frame
    cv2.imshow('frame',bin_img)
    
    # Exit if ESC key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()