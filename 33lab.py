# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:26:05 2024

@author: hdm 
"""

n = int(input("Nhập số nguyên dương N: "))
while n <= 0:
    n = int(input("Nhập lại số hợp lệ: "))
for i in range(1, n+1):
    if i * i == n:
        print(n, "là số chính phương")
        break 
else:
    print(n,"không là số chính phương")