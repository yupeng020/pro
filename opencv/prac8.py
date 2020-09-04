#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : prac8.py
#   Author      : ky-zyp 
#   Created date: 2020-09-04 15:00:05
#   Description : 
#
#================================================================

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('11.jpg', 0)
# 全局阀值
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# Otsu(大津)阀值
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# 高斯滤波后在用Otsu阀值
blur = cv.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# 绘制所有图像及直方图
images = [img, 0, th1,
          img, 0, th2,
          blur,0, th3]
titles = ['Original Image', 'Histogram', "Global Thresholding(v=127)",
          'Original Image', 'Histogram', "Ostu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()

