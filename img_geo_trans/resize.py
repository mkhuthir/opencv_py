#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

img = cv.imread("../_img/players.jpg",1)

# Scale
img_half = cv.resize(img, (0,0), fx=0.5, fy=0.5)
img_stretch = cv.resize(img, (600,600))
img_stretch_near = cv.resize(img, (600,600), interpolation=cv.INTER_NEAREST)

cv.imshow("Half",img_half)
cv.imshow("Stretch",img_stretch)
cv.imshow("Stretch near",img_stretch_near)

cv.waitKey(0)
cv.destroyAllWindows()