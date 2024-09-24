# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 19:15:59 2024

@author: huynhdieumy
"""
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
loai = [(a == b == c, "Tam giác đều"),
        (a == b or a == c or b == c, "Tam giác cân"),
        (a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2, "Tam giác vuông"),
        (a < b + c or b < a + c or c < a + b, "Tam giác thường")]
for dieukien, tamgiac in loai:
    if dieukien:
        print(tamgiac)
        break
else: 
        print("Đây không là tam giác!")
