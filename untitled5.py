# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:54:32 2024

@author: Student
"""

print("kiểm tra ba cạnh")
a = float(input("nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))
if a + b > c and b + c > a and a + c > b:
    print(a,b,c,"là ba cạnh của một tam giác")
else:
    print(a,b,c,"không phải là cạnh của một tam giác")    

            
