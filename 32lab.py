# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:51:19 2024

@author: L13
"""
kmdi = int(input("Nhập số km Taxi đi được: "))
tien = 0
for km in range(1, kmdi +1):
    if km == 1:
        tien += 15000
    elif 2 <= km <= 5:
        tien += 13500
    elif km < 6:
        tien += 11000
if km < 120:
    tien = tien * 0.9
print(f"Số tiền cước Taxi là {tien} đồng.")