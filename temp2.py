# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:57:28 2024

@author: Student
"""

date_input = input("nhập ngày tháng năm (dd/mm/yyyy hoặc dd-mm-yyyy):")
if '/' in date_input:
    separator = '/'
    parts = date_input.split('/')
elif '-' in date_input:
    separator = "-"
    parts = date_input.split('-')
else:
    print("ngày tháng năm không hợp lệ")
    exit()
if len(parts) !=3:
    print("ngày tháng năm không hợp lệ")
    exit()
day, month, year = parts
if not (day.isdigit() and month. isdigit() and year.isdigit()):
    print("ngày tháng năm không hợp lệ")
    exit()
day = int(day)
month = int(month)
year = int(year)
if year < 1:
    print("ngày tháng năm khoong hợp lệ")
    exit()
days_in_month = [31,29 if (year % 4 == 0 and year %100 !=0) or (year %400 ==0)else 28,31,30,31,30,31,31,30,31,30,31]
if day < 1 or day < days_in_month [month -1]:
    print("ngày tháng năm không hợp lệ")
else:
    print("ngày tháng năm hợp lệ")
    