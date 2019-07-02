"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:寻找1~9999完美数

Date    : 2019-07-02 12:24:05
Author  : Younth Yang (8593009@qq.com)
"""

for num in range(1,10000):
	sum=0
	for num2 in range(1,num):
		if num % num2 == 0 :
			sum += num2
	if num == sum:
		print(num)