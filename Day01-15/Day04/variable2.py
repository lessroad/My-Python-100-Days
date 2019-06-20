"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:用for循环实现1~100之间的偶数求和

Date    : 2019-06-19 10:12:22
Author  : Younth Yang (8593009@qq.com)
"""

sum=0
for x in range(2,101,2):
	sum+=x
	print(x)
print(sum)