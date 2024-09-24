# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:44:36 2024

@author: hdm 
"""
print("Tính S(n) = x + (x**2)/((1+2) + (x**3)/(1+2+3) + ... + (X**n)/(1+2+3+...n)")
x = float(input("Nhập số x: "))
n = int(input("Nhập số nguyên dương n: "))
tong = 0
ntang = 0
while n<=0:
    n=int(input("Nhập lại số n hợp lệ: "))
for i in range(1, n+1):
    ntang += i
    tong += (x**i)/ntang
print("Kết quả: ", tong)