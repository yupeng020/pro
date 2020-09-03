#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#================================================================
#   Copyright (C) 2020 * Ltd. All rights reserved.
#   
#   File name   : class.py
#   Author      : ky-zyp 
#   Created date: 2020-08-25 09:41:14
#   Description : 
#
#================================================================

"""熟悉类的用法和特性"""

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = 'global spam'


    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print('After nonlocal assignment:',spam)
    do_global()
    print('After global assignment:', spam)

scope_test()
print('In global scope:', spam)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

obj = Bag()
print(obj.addtwice(5))
