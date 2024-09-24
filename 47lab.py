# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:01:43 2024

@author: Huỳnh Diệu Mỹ 
"""
max_sum = 0
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,110):
            if 2*x + 7*y + 9*z == 979:
                tong = x+y+z
                if tong > max_sum:
                    max_sum = tong
                    solonnhat=[x,y,z]
print("Bộ nghiệm có tổng lớn nhất là: ", solonnhat, "với tổng là", max_sum)
