#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import cv2 as cv

# Read image in black/white format
bw_img = cv.imread('../_img/detect_blob.png', 0)
height, width = bw_img.shape[0:2]

# Threshold values to be used
thresh_min = 85
thresh_max = 255

# Do Binary threshold cv function (fast process)
ret, bin_img = cv.threshold(bw_img, thresh_min, thresh_max, cv.THRESH_BINARY)

# Show Results
cv.imshow("Org. Image",bw_img)
cv.imshow("Binary Thr.",bin_img)

# Wait for a key-press to exit
cv.waitKey(0)
cv.destroyAllWindows()