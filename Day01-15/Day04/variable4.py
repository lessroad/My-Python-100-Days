"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:输出乘法口诀表(九九表)

Date    : 2019-06-19 10:30:45
Author  : Younth Yang (8593009@qq.com)
"""

for i in range(1,10):
	for j in range(1,i+1):
		print('%d * %d = %d'%(j,i,i*j),end='\t')
	print('\n')