#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import cv2 as cv

# Read Image
img = cv.imread('../_img/fruits.jpg')

print("Height=",len(img))
print("Width=",len(img[0]))
print("Channels=", len(img[0][0]))
print('----')
print("Shape=", img.shape)
print('----')
print("Data Type=",img.dtype)
print("Pixel(10,5)=",img[10, 5])
print('----')
print("Image Size=",img.size)
