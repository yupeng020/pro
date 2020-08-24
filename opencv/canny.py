#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : canny.py
#   Author      : ky-zyp 
#   Created date: 2020-08-19 17:16:14
#   Description : 
#
#================================================================

import cv2
import numpy as np


img = cv2.imread("11.jpg", 0)
cv2.imwrite("11.png", cv2.Canny(img, 200, 300))
cv2.imshow("ceshi",cv2.imread("11.png"))
cv2.waitKey()
cv2.destroyAllWindows()

