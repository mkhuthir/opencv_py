#!/usr/bin/python3

import numpy as np
import cv2

# Load BGR image
bgr = cv2.imread("../img/butterfly.jpg", 1)

# Show BGR image
cv2.imshow("BGR",bgr)
cv2.moveWindow("BGR",0,0)

print(bgr.shape)
height,width,channels = bgr.shape

# Convert image from BGR to Gray
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
cv2.imwrite("../img/butterfly_gray.jpg",gray)

cv2.imshow("Gray",gray)
cv2.moveWindow("Gray",width,0)

cv2.waitKey(0)
cv2.destroyAllWindows()