#!/usr/bin/python3

import numpy as np
import cv2

# Load image in BGR colors
img = cv2.imread('../img/faces.jpeg',1)

# Convert to HSV and split into channels
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# Concatenate 3 channels in one image and display it
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("Split HSV",hsv_split)

# Apply threshold on S channel
ret, min_sat = cv2.threshold(s,40,255, cv2.THRESH_BINARY)
cv2.imshow("Sat Filter",min_sat)

# Apply threshold on H channel
ret, max_hue = cv2.threshold(h,15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter",max_hue)

# Skin color will be S and H thresholded
final = cv2.bitwise_and(min_sat,max_hue)
cv2.imshow("Final",final)
cv2.imshow("Original",img)

# wait for key-press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
