#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import cv2 as cv

img = cv.imread("../_img/players.jpg",1)

# Rotation
M = cv.getRotationMatrix2D((0,0), -30, 1)
rotated = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Show image
cv.imshow("Rotated",rotated)

cv.waitKey(0)
cv.destroyAllWindows()