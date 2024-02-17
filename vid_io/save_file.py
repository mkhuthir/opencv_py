#!/usr/bin/python3

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../vid/output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # do operation on the frame
        frame = cv2.flip(frame,0)

        # write the frame
        out.write(frame)

        # Show the frame
        cv2.imshow('frame',frame)

        # Exit if ESC key is pressed
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()