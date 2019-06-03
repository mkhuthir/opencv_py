#!/usr/bin/python3

import cv2

img = cv2.imread("../img/players.jpg",1)

# Rotation
M = cv2.getRotationMatrix2D((0,0), -30, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# Show image
cv2.imshow("Rotated",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()