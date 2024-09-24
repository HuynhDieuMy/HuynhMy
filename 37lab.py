# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:13:14 2024

@author: hdm
"""
n = int(input("Nhập vào số n (số chẵn, lớn hơn 0): "))
ketqua = 0
while n % 2 != 0 and n <= 0:
    n = int(input("Nhập lại số n theo điều kiện: "))
for i in range(2, n+1, 2):
    ketqua += i
print("Kết quả là: ", ketqua)