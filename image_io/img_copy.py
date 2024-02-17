#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Create image using numpy.zeros function
# Black Image 8 bits
img_black = np.zeros([150,200,3],'uint8')
cv.imshow("Black",img_black)

# White Image 16 bit
ones = np.ones([150,200,3],'uint16')
img_white = ones * (2**16-1)
cv.imshow("White",img_white)

# Blue Image 8 bits
img_red = img_black.copy()
img_red[:,:] = [255,0,0]
cv.imshow("Blue",img_red)

# Green Image 8 bits
img_red = img_black.copy()
img_red[:,:] = [0,255,0]
cv.imshow("Green",img_red)

# Red Image 8 bits
img_red = img_black.copy()
img_red[:,:] = [0,0,255]
cv.imshow("Red",img_red)

cv.waitKey(0)
cv.destroyAllWindows()
