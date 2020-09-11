#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : prac10.py
#   Author      : ky-zyp 
#   Created date: 2020-09-07 09:49:24
#   Description : 
#
#================================================================

"""霍夫变换检测圆"""

import numpy as np
import cv2 as cv

img = cv.imread('timg.jpg', 0)
img = cv.medianBlur(img, 5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30,
        minRadius=10, maxRadius=50)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # 绘制外圆
    cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # 绘制圆心
    cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
cv.imshow('detected circles', cimg)
cv.waitKey(0)
cv.destroyAllWindows()

