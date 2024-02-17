#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import cv2 as cv

# Read Image
img = cv.imread('../img/fruits.jpg')

# Show image
cv.namedWindow('image',cv.WINDOW_NORMAL)
cv.imshow('image',img)

# Wait for a key
cv.waitKey(0)
cv.destroyAllWindows()

