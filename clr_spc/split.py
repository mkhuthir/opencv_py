#!/usr/bin/python3

import numpy as np
import cv2

# load BGR image
bgr = cv2.imread("../img/butterfly.jpg", 1)

# Show BGR image
cv2.imshow("Image",bgr)
cv2.moveWindow("Image",0,0)

print(bgr.shape)
height,width,channels = bgr.shape

# Split BGR image
b,g,r = cv2.split(bgr)

# Create 3xwidth empty image
rgb_split = np.empty([height,width*3,3],'uint8')

# Copy channels into empty image
rgb_split[:, 0:width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])

# Show image
cv2.imshow("Split BGR",rgb_split)
cv2.moveWindow("Split BGR",0,height)

# Convert BGR to HSV and split it
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)

# Show image
cv2.imshow("Split HSV",hsv_split)
cv2.moveWindow("Split HSV",0,height*2)

cv2.waitKey(0)
cv2.destroyAllWindows()

