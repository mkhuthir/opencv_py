#!/usr/bin/python3

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read sample image
org_img=cv.imread('../_img/fruits.jpg')                

# Convert color space from BGR to HSV
hsv_img = cv.cvtColor(org_img,cv.COLOR_BGR2HSV)

# Threshold min and max HSV limits
min = np.array([10 ,50 ,50 ],np.uint8)
max = np.array([20,255,255],np.uint8)

# Creat mask using HSV color space
mask = cv.inRange(hsv_img,min,max)

# Apply the mask on BGR color space
thr_img = cv.bitwise_and(org_img,org_img,mask = mask)

# Show images
cv.imshow("Org. Image", org_img)
cv.imshow("Thr. Image", thr_img)
print (thr_img.shape)

# Wait for a key-press then exit
cv.waitKey(0)
cv.destroyAllWindows()




