#!/usr/bin/python3

import cv2 as cv
import numpy as np

image = cv.imread("../_img/thresh.jpg")
cv.imshow("Original",image)

kernel = np.ones((5,5),'uint8')
erode = cv.erode(image,kernel,iterations=1)
cv.imshow("Erode",erode)

cv.waitKey(0)
cv.destroyAllWindows()