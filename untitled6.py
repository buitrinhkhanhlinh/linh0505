# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:34:05 2024

@author: Student
"""

print("kiểm tra ba cạnh")
a = float(input("nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))
if a + b > c and b + c > a and a + c > b:
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print(a,b,c, "là ba cạnh của tam giác vuông")
    elif a==b and b==c:
        print(a,b,c,"là ba cạnh của tam giác đều")
    elif a==b or b==c or a==c:
        print("là ba cạnh của tam giác cân")
    else:
        print(a,b,c,"là ba cạnh tam giác thường")
else: 
    print(a,b,c,"không là ba cạnh của một tam giác")
    