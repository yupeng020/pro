#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : prac5.py
#   Author      : ky-zyp 
#   Created date: 2020-09-04 08:59:25
#   Description : 
#
#================================================================

"""一些高级演示功能"""
import numpy as np
import cv2 as cv

drawing = False # if mouse click,that is True 
mode = True # if true,draw a rectangle,or press m key to draw a cuve
ix, iy = -1, -1
# 鼠标回调函数

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x,y), 5, (0, 0, 255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing == False
        if mode == True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)


def nothing(x):
    pass
# 创建一个黑色图像，一个窗口
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image0')
# 创建颜色变化的轨迹栏
cv.createTrackbar('R', 'image0', 0, 255, nothing)
cv.createTrackbar('G', 'image0', 0, 255, nothing)
cv.createTrackbar('B', 'image0', 0, 255, nothing)
# 为ON/OFF功能创建开关
switch = '0:OFF \n1:ON'
cv.createTrackbar(switch, 'image0', 0, 1, nothing)
while(1):
    cv.imshow('image0', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # 得到四条轨迹的当前位置
    r = cv.getTrackbarPos('R', 'image0')
    g = cv.getTrackbarPos('G', 'image0')
    b = cv.getTrackbarPos('B', 'image0')
    s = cv.getTrackbarPos(switch, 'image0')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv.destroyAllWindows()


