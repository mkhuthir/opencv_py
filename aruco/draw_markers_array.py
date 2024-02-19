#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.cm as cm

aruco_dict = cv.aruco.Dictionary_get(cv.aruco.DICT_6X6_100)

fig = plt.figure()

x = 3
y = 3

for i in range(0, x*y):
    ax = fig.add_subplot(y,x, i+1)
    img = cv.aruco.drawMarker(aruco_dict,i, 320)
    plt.imshow(img, cmap = cm.gray, interpolation = "nearest")
    ax.axis("off")

plt.savefig("markers.jpeg")
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
