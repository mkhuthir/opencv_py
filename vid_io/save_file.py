#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('../_vid/output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # do operation on the frame
        frame = cv.flip(frame,0)

        # write the frame
        out.write(frame)

        # Show the frame
        cv.imshow('frame',frame)

        # Exit if ESC key is pressed
        if cv.waitKey(20) & 0xFF == 27:
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()