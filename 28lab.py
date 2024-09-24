# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:23:12 2024

@author: huynhdieumy 
"""
while True:
    n = input("Nhập số nguyên dương n: ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        break
    else:
        print("Vui lòng nhập số hợp lệ!")
        continue
print(f"Các ước của {n} là: ")
for i in range(1,n):
    if n % i == 0:
        print(i, end = '\t')
        