#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Threshold values to be used
thresh_min = 85
thresh_max = 255

# Start Capture
cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert from BGR to Gray
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Do Binary threshold cv function (fast process)
    ret, bin_img = cv.threshold(gray, thresh_min, thresh_max, cv.THRESH_BINARY)

    # Display the resulting frame
    cv.imshow('frame',bin_img)
    
    # Exit if ESC key is pressed
    if cv.waitKey(20) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()