#!/usr/bin/python3

import cv2
import matplotlib.pyplot as plt

# Read sample BGR image
bgr_img = cv2.imread('../img/fruits.jpg')
print ("Image Shape",bgr_img.shape)

# Convert BGR to RGB for Matplotlib use.
rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB) 

# Show images using Matplotlib
# note that BGR will show wrong colors since Matplotlib is using RGB format
f, ax = plt.subplots(1, 2, figsize=(24,12))
ax[0].imshow(bgr_img)
ax[0].set_title('BGR Image', fontsize=20)

ax[1].imshow(rgb_img)
ax[1].set_title('RGB Image', fontsize=20)
       
plt.show()