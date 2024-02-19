#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import cv2 as cv

# Read image
image = cv.imread("../_img/thresh.jpg")
cv.imshow("Original",image)

# Apply filter then show result
blur = cv.GaussianBlur(image, (5,55),0)
cv.imshow("Blur",blur)

# Wait for a key-press then exit
cv.waitKey(0)
cv.destroyAllWindows()