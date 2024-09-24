# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:38:14 2024

@author: hdm 
"""
n = int(input("Nhập vào số n: "))
ketqua = 0
while n == 0 :
    n = int(input("n không được bằng 0, nhập lại số n: "))
for i in range(1, n+1):
    ketqua += 1/i
print("Kết quả là: ", ketqua)
