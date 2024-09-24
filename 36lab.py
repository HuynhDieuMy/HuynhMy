# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:05:15 2024

@author: hdm 
"""
print("Tính S = 1**2 + 2**2 + 3**2 + ... + n**2")
n = int(input("Nhập số nguyên n và lớn hơn 0: "))
ketqua = 0 
while n <= 0 :
    n = int(input("Nhập lại số nguyên n theo điều kiện: "))
for i in range(1, n+1) :
    ketqua += i**2    
print("Kết quả là: ", ketqua)