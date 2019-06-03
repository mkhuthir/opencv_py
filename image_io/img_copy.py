#!/usr/bin/python3

import numpy as np
import cv2

# Create image using numpy.zeros function
# Black Image 8 bits
img_black = np.zeros([150,200,3],'uint8')
cv2.imshow("Black",img_black)

# White Image 16 bit
ones = np.ones([150,200,3],'uint16')
img_white = ones * (2**16-1)
cv2.imshow("White",img_white)

# Blue Image 8 bits
img_red = img_black.copy()
img_red[:,:] = [255,0,0]
cv2.imshow("Blue",img_red)

# Green Image 8 bits
img_red = img_black.copy()
img_red[:,:] = [0,255,0]
cv2.imshow("Green",img_red)

# Red Image 8 bits
img_red = img_black.copy()
img_red[:,:] = [0,0,255]
cv2.imshow("Red",img_red)

cv2.waitKey(0)
cv2.destroyAllWindows()
