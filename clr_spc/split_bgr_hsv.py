#!/usr/bin/python3

import numpy as np
import cv2 as cv

# load BGR image
bgr = cv.imread("../_img/butterfly.jpg", 1)

# Show BGR image
cv.imshow("Image",bgr)
cv.moveWindow("Image",0,0)

print(bgr.shape)
height,width,channels = bgr.shape

# Split BGR image
b,g,r = cv.split(bgr)

# Create 3xwidth empty image
rgb_split = np.empty([height,width*3,3],'uint8')

# Copy channels into empty image
rgb_split[:, 0:width] = cv.merge([b,b,b])
rgb_split[:, width:width*2] = cv.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv.merge([r,r,r])

# Show image
cv.imshow("Split BGR",rgb_split)
cv.moveWindow("Split BGR",0,height)

# Convert BGR to HSV and split it
hsv = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
h,s,v = cv.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)

# Show image
cv.imshow("Split HSV",hsv_split)
cv.moveWindow("Split HSV",0,height*2)

cv.waitKey(0)
cv.destroyAllWindows()

