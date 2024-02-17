#!/usr/bin/python3

import cv2 as cv
import numpy as np

image = cv.imread("../img/thresh.jpg")
cv.imshow("Original",image)

kernel = np.ones((5,5),'uint8')
dilate = cv.dilate(image,kernel,iterations=1)
cv.imshow("Dilate",dilate)

cv.waitKey(0)
cv.destroyAllWindows()