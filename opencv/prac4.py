#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : prac4.py
#   Author      : ky-zyp 
#   Created date: 2020-09-03 15:56:45
#   Description : 
#
#================================================================
"""鼠标事件"""
import numpy as np
import cv2 as cv


# 鼠标回调函数
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)

# 创建一个黑色图像。一个窗口，并绑定到窗口
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:  # 按ESC退出
        break
cv.destroyAllWindows()

