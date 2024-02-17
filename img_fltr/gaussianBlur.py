#!/usr/bin/python3

import cv2

# Read image
image = cv2.imread("../img/thresh.jpg")
cv2.imshow("Original",image)

# Apply filter then show result
blur = cv2.GaussianBlur(image, (5,55),0)
cv2.imshow("Blur",blur)

# Wait for a key-press then exit
cv2.waitKey(0)
cv2.destroyAllWindows()