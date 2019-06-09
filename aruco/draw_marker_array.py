#!/usr/bin/python3

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_100)

fig = plt.figure()

x = 4
y = 4

for i in range(0, x*y):
    ax = fig.add_subplot(y,x, i+1)
    img = cv2.aruco.drawMarker(aruco_dict,i, 320)
    plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
    ax.axis("off")

plt.savefig("markers.jpeg")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
