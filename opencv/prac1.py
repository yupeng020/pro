#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : prac1.py
#   Author      : ky-zyp 
#   Created date: 2020-09-03 14:45:14
#   Description : 
#
#================================================================

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('11.jpg', 0)
cv.imshow('hehe', img)
cv.waitKey(0)
cv.destroyAllWindows()
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()


