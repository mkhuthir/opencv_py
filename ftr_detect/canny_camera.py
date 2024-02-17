#!/usr/bin/python3

import numpy as np
import cv2

# Start Capture
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Apply Canny filter
    canny = cv2.Canny(frame, 100, 70)

    # Display the resulting frame
    cv2.imshow('frame',canny)
    
    # Exit if ESC key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()