#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : prac7.py
#   Author      : ky-zyp 
#   Created date: 2020-09-04 14:30:03
#   Description : 
#
#================================================================

"""对象追踪"""
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    _, frame = cap.read()
    # 转换颜色空间到HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 定义HSV中蓝色的范围
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # 设置HSV的阀值，使得只取蓝色
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # 将阀值和图像相加
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('maskla', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
