#!/usr/bin/python3

import numpy as np
import cv2 as cv

marker_id = 0
marker_pixels = 320
marker_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_100)

marker_img = cv.aruco.drawMarker(marker_dict, marker_id, marker_pixels)

cv.imshow('aruco code id '+str(marker_id),marker_img)

cv.imwrite("marker_id"+str(marker_id)+".jpg", marker_img)

cv.waitKey(0)
cv.destroyAllWindows()
