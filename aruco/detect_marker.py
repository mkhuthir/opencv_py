#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

marker_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_100)
parameters =  cv.aruco.DetectorParameters_create()
color = (0,255,0)

while(True):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = cv.aruco.detectMarkers(gray, marker_dict, parameters=parameters)

    frame = cv.aruco.drawDetectedMarkers(frame, corners, ids, color)

    cv.imshow('Video',frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
