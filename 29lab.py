# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:50:00 2024

@author: huynhdieumy
"""
n = int(input("Nhập vào số nguyên n: "))
tong = 0
while n <= 0:
    n = int(input("N phải là số nguyên dương: "))
for i in str(n):
    tong += int(i)
print(f"Tổng các số của {n} là: {tong}")