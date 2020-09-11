#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : prac11.py
#   Author      : ky-zyp 
#   Created date: 2020-09-07 10:55:13
#   Description : 
#
#================================================================

"""高速拐角检测器"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('22.jpg', 0)
# 用默认值初始化Fast对象
fast = cv.FastFeatureDetector_create()
# 寻找并绘制关键点
kp = fast.detect(img, None)
img2 = cv.drawKeypoints(img, kp, None, color=(255, 0, 0))
cv.imwrite('fast_true.png', img2)
# 关闭非极大抑制
fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)
print("Total Keypionts without nonmaxSuppression: {}".format(len(kp)))
img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
cv.imwrite('fast_false.png', img3)

