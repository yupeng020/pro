#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : detectCircles.py
#   Author      : ky-zyp 
#   Created date: 2020-08-20 14:33:59
#   Description : 
#
#================================================================

import cv2
import numpy as np

planets = cv2.imread('planet.jpg')
gray_img = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(gray_img, 5)

