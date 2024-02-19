#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Start Capture
cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Apply Canny filter
    canny = cv.Canny(frame, 100, 70)

    # Display the resulting frame
    cv.imshow('frame',canny)
    
    # Exit if ESC key is pressed
    if cv.waitKey(20) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()