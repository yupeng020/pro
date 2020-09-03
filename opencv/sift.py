#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : sift.py
#   Author      : ky-zyp 
#   Created date: 2020-08-24 14:39:52
#   Description : 
#
#================================================================

import cv2
import sys
import numpy as np

# imgpath = sys.argv[1]
img = cv2.imread('city.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptor = sift.detectAndCompute(gray, None)

img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints,
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color=(51, 163, 236))

cv2.imshow('sift', img)
while True:
    if cv2.waitKey(1000) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()

