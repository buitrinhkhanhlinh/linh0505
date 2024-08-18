# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:35:55 2024

@author: Student
"""

print("Tính phương trình bậc nhất: ax + b = 0")
a = float(input("nhập giá trị của a: "))
b = float(input("nhập giá trị của b: "))
if a !=0:
    x = -b/a
    print("nghiệm của phương trình là:", x)
else:
    if b==0:
        print("phương trình vô số nghiệm")
    else:
        print("phương trình vô nghiệm")