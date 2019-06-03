#!/usr/bin/python3

import numpy as np
import cv2

# Read image in black/white format
bw = cv2.imread('../img/detect_blob.png', 0)
height, width = bw.shape[0:2]

# Create a black image same size of bw
binary = np.zeros([height,width,1],'uint8')

# Threshold value to be used
thresh = 85

# Do binary threshold using loop (slow process)
for row in range(0,height):
	for col in range(0, width):
		if bw[row][col]>thresh:
			binary[row][col]=255

# Show Results
cv2.imshow("Org. Image",bw)
cv2.imshow("Slow Binary Thr.",binary)

# Wait for a key-press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()