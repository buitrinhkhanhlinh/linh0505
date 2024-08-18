# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = float(input("nhập số km: "))
if a <= 1:
    d = 20000
    print("tiền taxi là: ", d)
elif a <= 3:
    d = a*13000
    print("tiền taxi là: ", d)
elif a <= 8:
    d = 3*13000 + (a-3)*12000
    print("tiền taxi là: ", d)
elif a > 8:
    d= 3*13000 + 5*12000 + (a-8)*10000
    print("tiền taxi là: ", d)
if d > 100000:
    d = d*0.92
    print("bạn được giảm 10%, tiền taxi của bạn là: ", d)
