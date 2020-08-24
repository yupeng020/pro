#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : test1.py
#   Author      : ky-zyp 
#   Created date: 2020-08-20 09:48:57
#   Description : 
#
#================================================================
"""一个小练习"""
"""opencv3中findContours返回三个值，但是在opencv4中只返回两个值,不再返回修改后
的图像，而只返回图像轮廓和它们的层次"""

import cv2
import numpy as np

img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255

ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()

