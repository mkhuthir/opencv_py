#!/usr/bin/python3

import numpy as np
import cv2

marker_id = 0
marker_pixels = 320
marker_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_100)

marker_img = cv2.aruco.drawMarker(marker_dict, marker_id, marker_pixels)

cv2.imshow('aruco code id '+str(marker_id),marker_img)

cv2.imwrite("marker_id"+str(marker_id)+".jpg", marker_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
