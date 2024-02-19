#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

# Load image in BGR colors
img = cv.imread('../_img/faces1.jpeg',1)

# Convert to HSV and split into channels
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# Concatenate 3 channels in one image and display it
hsv_split = np.concatenate((h,s,v), axis=1)
cv.imshow("Split HSV",hsv_split)

# Apply threshold on S channel
ret, min_sat = cv.threshold(s,40,255, cv.THRESH_BINARY)
cv.imshow("Sat Filter",min_sat)

# Apply threshold on H channel
ret, max_hue = cv.threshold(h,15, 255, cv.THRESH_BINARY_INV)
cv.imshow("Hue Filter",max_hue)

# Skin color will be S and H thresholded
final = cv.bitwise_and(min_sat,max_hue)
cv.imshow("Final",final)
cv.imshow("Original",img)

# wait for key-press to exit
cv.waitKey(0)
cv.destroyAllWindows()
