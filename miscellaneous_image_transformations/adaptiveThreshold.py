#!/usr/bin/python3

import cv2

# Read image in black/white format
bw_img = cv2.imread('../img/sudoku.png', 0)
height, width = bw_img.shape[0:2]

# Threshold values to be used
threshMax = 255
adaptiveMethod = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
thresholdType = cv2.THRESH_BINARY
blockSize = 251
C = 1

# Do Binary threshold cv2 function (fast process)
bin_img = cv2.adaptiveThreshold(bw_img, threshMax, adaptiveMethod, thresholdType, blockSize, C)

# Show Results
cv2.imshow("Org. Image",bw_img)
cv2.imshow("Binary Thr.",bin_img)

# Wait for a key-press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()