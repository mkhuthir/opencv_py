#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024


import numpy as np
import cv2 as cv

# Load BGR image
bgr = cv.imread("../_img/butterfly.jpg", 1)

# Show BGR image
cv.imshow("BGR",bgr)
cv.moveWindow("BGR",0,0)

print(bgr.shape)
height,width,channels = bgr.shape

# Convert image from BGR to Gray
gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
cv.imwrite("../_img/butterfly_gray.jpg",gray)

cv.imshow("Gray",gray)
cv.moveWindow("Gray",width,0)

cv.waitKey(0)
cv.destroyAllWindows()