"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:输入一个正整数判断它是不是素数

Date    : 2019-06-20 15:45:35
Author  : Younth Yang (8593009@qq.com)
"""

from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)