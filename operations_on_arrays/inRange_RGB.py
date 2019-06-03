#!/usr/bin/python3

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read sample image
org_img = cv2.imread('../img/rgb_test.png')

# Threshold min and max BGR limits
min = np.array([0,0,0  ],np.uint8)
max = np.array([0,0,255],np.uint8)

# Create a mask
mask = cv2.inRange(org_img,min,max)

# Apply mask
thr_img = cv2.bitwise_and(org_img,org_img,mask = mask)      
print ("Image Shape",org_img.shape)

# Show images
cv2.imshow("Org. Image", org_img)
cv2.imshow("Threshold Image", thr_img)

# Wait for a key-press then exit
cv2.waitKey(0)
cv2.destroyAllWindows()