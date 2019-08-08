"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:作用域

Date    : 2019-08-08 11:23:47
Author  : Younth Yang (8593009@qq.com)
"""

def foo():
	b='hello'
	c=101
	print(a)

	def bar():
		nonlocal c
		
		c=102

		print(a)
		print(b)
		print(c)

	bar()
	print(c)

if __name__ == '__main__':
	a = 100

	foo()

	print(a)
