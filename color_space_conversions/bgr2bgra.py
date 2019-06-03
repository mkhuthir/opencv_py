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

# Split channels
b = bgr[:,:,0]
g = bgr[:,:,1]
r = bgr[:,:,2]

# create new image BGR and add G as transperancy channel
bgra = cv2.merge((b,g,r,g))
cv2.imwrite("../img/butterfly_bgra.png",bgra)

cv2.imshow("BGRA",bgra)
cv2.moveWindow("BGRA",width,0)

cv2.waitKey(0)
cv2.destroyAllWindows()

