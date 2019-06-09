#!/usr/bin/python3

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

marker_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_100)
parameters =  cv2.aruco.DetectorParameters_create()
color = (0,255,0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, marker_dict, parameters=parameters)

    frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids, color)

    cv2.imshow('Video',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
