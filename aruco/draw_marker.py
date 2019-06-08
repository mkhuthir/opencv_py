#!/usr/bin/python3

import numpy as np
import cv2

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
print(aruco_dict)

# second parameter is id number
# last parameter is total image size

img = cv2.aruco.drawMarker(aruco_dict, 2, 700)
cv2.imwrite("test_marker.jpg", img)

cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
