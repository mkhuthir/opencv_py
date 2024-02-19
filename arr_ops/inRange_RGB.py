#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read sample image
org_img = cv.imread('../_img/rgb_test.png')

# Threshold min and max BGR limits
min = np.array([0,0,0  ],np.uint8)
max = np.array([0,0,255],np.uint8)

# Create a mask
mask = cv.inRange(org_img,min,max)

# Apply mask
thr_img = cv.bitwise_and(org_img,org_img,mask = mask)      
print ("Image Shape",org_img.shape)

# Show images
cv.imshow("Org. Image", org_img)
cv.imshow("Threshold Image", thr_img)

# Wait for a key-press then exit
cv.waitKey(0)
cv.destroyAllWindows()