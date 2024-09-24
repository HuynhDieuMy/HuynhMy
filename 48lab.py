# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:05:17 2024

@author: Huỳnh Diệu Mỹ 
"""
min_sum = float('inf')
for x in range(1,490):
    for y in range(1,140):
        for z in range(1,110):
            if 2*x + 7*y + 9*z == 979:
                tong = x + y + z
                if tong < min_sum:
                    min_sum = tong 
                    sonhonhat = [x,y,z]
print("Bộ nghiệm có tổng nhỏ nhất là: ",sonhonhat, "với tổng là", min_sum)