# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:50:42 2024

@author: Huỳnh Diệu Mỹ
"""
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,110):
            if 2*x + 7*y + 9*z == 979:
                print([x,y,z], end='\t' )