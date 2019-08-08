"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:判断回文数

Date    : 2019-08-08 10:59:16
Author  : Younth Yang (8593009@qq.com)
"""

a = int(input("请输入一个数:"))

def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        print(temp)
        total = total * 10 + temp % 10
        print(total)
        temp //= 10
        print(temp)

    return total == num

print("%d,%d"%(a,is_palindrome(a)))

for x in range(1,10):
	print(x)