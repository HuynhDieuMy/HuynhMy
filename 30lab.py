# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 19:03:10 2024

@author:  huynhdieumy
"""
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
songay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (nam % 400 ==0) or (nam % 4 ==0 and nam % 100 != 0):
    songay[1] = 29
for i in range(1,13):
    if thang == i:
        print(f"Tháng {thang} năm {nam} có {songay[i-1]} ngày")
        break