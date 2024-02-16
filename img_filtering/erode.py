#!/usr/bin/python3

import cv2
import numpy as np

image = cv2.imread("../img/thresh.jpg")
cv2.imshow("Original",image)

kernel = np.ones((5,5),'uint8')
erode = cv2.erode(image,kernel,iterations=1)
cv2.imshow("Erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()