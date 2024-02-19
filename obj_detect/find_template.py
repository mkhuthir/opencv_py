#!/usr/bin/python3
# Muthanna Alwahash
# Feb 2024

import numpy as np
import cv2 as cv

template = cv.imread('../_img/template.jpg',0)
frame = cv.imread("../_img/players.jpg",0)

cv.imshow("Frame",frame)
cv.imshow("Template",template)

# Match TemplateS
result = cv.matchTemplate(frame, template, cv.TM_CCOEFF_NORMED)

# Use minMaxLoc to find the maximum match
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
print(max_val,max_loc)

# Draw circle on the max_loc
cv.circle(result,max_loc, 15,255,2)
cv.imshow("Matching",result)

cv.waitKey(0)
cv.destroyAllWindows()