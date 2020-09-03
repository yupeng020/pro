#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : prac3.py
#   Author      : ky-zyp 
#   Created date: 2020-09-03 15:31:39
#   Description : 
#
#================================================================

"""绘制各种形状"""
import numpy as np
import cv2 as cv

# 创建黑色图像
img = np.zeros((512, 512, 3), np.uint8)
# 绘制一条厚度为5的蓝色对角线
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 绘制椭圆，中心位置(x,y),长短轴长度，沿逆时针旋转的角度
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 270, 255, -1)
# 画圆
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
cv.imshow("hehe", img)
cv.waitKey()
cv.destroyAllWindows()

