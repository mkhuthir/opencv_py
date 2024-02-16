#!/usr/bin/python3

import numpy as np
import cv2

template = cv2.imread('../img/template.jpg',0)
frame = cv2.imread("../img/players.jpg",0)

cv2.imshow("Frame",frame)
cv2.imshow("Template",template)

# Match TemplateS
result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)

# Use minMaxLoc to find the maximum match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val,max_loc)

# Draw circle on the max_loc
cv2.circle(result,max_loc, 15,255,2)
cv2.imshow("Matching",result)

cv2.waitKey(0)
cv2.destroyAllWindows()