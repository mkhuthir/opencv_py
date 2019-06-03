#!/usr/bin/python3

import cv2

# Read Image
img = cv2.imread('../img/fruits.jpg')

# Show image
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)

# Wait for a key
cv2.waitKey(0)
cv2.destroyAllWindows()

