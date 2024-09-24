# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:27:08 2024

@author: Huynh Dieu My
"""
n = int(input("Nhập vào số n cần tính: "))
tong = 0 
for i in range(1, n+1):
    tong += i
print("Kết quả thu được là: ", tong)
