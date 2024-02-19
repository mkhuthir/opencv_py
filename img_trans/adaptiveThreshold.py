#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024


import cv2 as cv

# Read image in black/white format
bw_img = cv.imread('../_img/sudoku.png', 0)
height, width = bw_img.shape[0:2]

# Threshold values to be used
threshMax = 255
adaptiveMethod = cv.ADAPTIVE_THRESH_GAUSSIAN_C
thresholdType = cv.THRESH_BINARY
blockSize = 251
C = 1

# Do Binary threshold cv function (fast process)
bin_img = cv.adaptiveThreshold(bw_img, threshMax, adaptiveMethod, thresholdType, blockSize, C)

# Show Results
cv.imshow("Org. Image",bw_img)
cv.imshow("Binary Thr.",bin_img)

# Wait for a key-press to exit
cv.waitKey(0)
cv.destroyAllWindows()