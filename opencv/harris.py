#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : harris.py
#   Author      : ky-zyp 
#   Created date: 2020-08-24 09:57:13
#   Description : 
#
#================================================================

import cv2
import numpy as np


img = cv2.imread('chess.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 23, 0.04)
img[dst>0.01 *dst.max()] = [0, 0, 255]
while True:
    cv2.imshow('corners', img)
    if cv2.waitKey(1000) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()



