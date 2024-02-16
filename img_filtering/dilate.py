#!/usr/bin/python3

import cv2
import numpy as np

image = cv2.imread("../img/thresh.jpg")
cv2.imshow("Original",image)

kernel = np.ones((5,5),'uint8')
dilate = cv2.dilate(image,kernel,iterations=1)
cv2.imshow("Dilate",dilate)

cv2.waitKey(0)
cv2.destroyAllWindows()