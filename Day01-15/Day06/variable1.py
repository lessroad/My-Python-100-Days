"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:求阶乘

Date    : 2019-07-02 13:21:32
Author  : Younth Yang (8593009@qq.com)
"""

def factorial(num):
	"""
	    求阶乘
	    
	    :param num: 非负整数
	    :return: num的阶乘
	"""
	result = 1
	for x in range(1,num+1):
		result *= x
	return result

m=int(input("m="))
n=int(input("n="))


print(factorial(m) // factorial(n) // factorial(m-n))