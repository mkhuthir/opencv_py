#!/usr/bin/python3

import cv2

# Read image in black/white format
bw_img = cv2.imread('../img/detect_blob.png', 0)
height, width = bw_img.shape[0:2]

# Threshold values to be used
thresh_min = 85
thresh_max = 255

# Do Binary threshold cv2 function (fast process)
ret, bin_img = cv2.threshold(bw_img, thresh_min, thresh_max, cv2.THRESH_BINARY)

# Show Results
cv2.imshow("Org. Image",bw_img)
cv2.imshow("Binary Thr.",bin_img)

# Wait for a key-press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()