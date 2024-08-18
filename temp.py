# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
distance = float(input("nhập độ dài đoạn đường đến trường(m): "))
if distance < 300:
    print("đường đến trường quá gần. Thôi! Đi bộ")
elif distance > 1200:
    print("Đường đến trường xa quá. Thôi! Đi xe máy")
elif distance >= 300 and distance <= 700:
    print("Đường đến trường không xa. Thôi! Đi xe đạp")
else:
    print(" kHông xác định")
    