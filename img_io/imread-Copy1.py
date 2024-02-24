#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import cv2 as cv

# Read Image
img = cv.imread('../_img/love.png')

# Show image
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.imshow('image',img)

# Wait for a key
cv.waitKey(0)
cv.destroyAllWindows()

