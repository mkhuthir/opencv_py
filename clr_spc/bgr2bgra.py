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

# Split channels
b = bgr[:,:,0]
g = bgr[:,:,1]
r = bgr[:,:,2]

# create new image BGR and add G as transperancy channel
bgra = cv.merge((b,g,r,g))
cv.imwrite("../_img/butterfly_bgra.png",bgra)

cv.imshow("BGRA",bgra)
cv.moveWindow("BGRA",width+10,0)

cv.waitKey(0)
cv.destroyAllWindows()

