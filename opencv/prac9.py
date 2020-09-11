#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : prac9.py
#   Author      : ky-zyp 
#   Created date: 2020-09-04 16:19:57
#   Description : 
#
#================================================================

"""霍夫变换检测直线"""


import cv2 as cv
import numpy as np

img = cv.imread('city.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100,
        maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv.imwrite('houghlines5.jpg', img)



