"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:水仙花数

Date    : 2019-07-02 12:14:05
Author  : Younth Yang (8593009@qq.com)
"""

for num in range(100,1000):
	low = num % 10
	mid = num // 10 % 10
	hig = num // 100
	if num == low ** 3 + mid ** 3 + hig ** 3:
		print(num)