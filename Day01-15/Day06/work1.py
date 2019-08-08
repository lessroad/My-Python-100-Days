"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:

Date    : 2019-08-08 10:41:06
Author  : Younth Yang (8593009@qq.com)
"""

def gcd(x, y):
	(x,y)=(y,x) if x>y else(x,y)

	print("%d,%d"%(x,y))

	for factor in range(x, 0,-1):
		if x % factor == 0 and y % factor == 0:
			a = factor
			break


	b = x*y // a

	print(a)
	print(b)

gcd(16,30)
