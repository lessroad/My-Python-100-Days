"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:分段函数求值

		        3x - 5  (x > 1)
		f(x) =  x + 2   (-1 <= x <= 1)
		        5x + 3  (x < -1)


Date    : 2019-05-24 14:25:55
Author  : Younth Yang (8593009@qq.com)
"""

x=float(input('x = '))
if x>1:
	fx=3*x -5
elif x>=-1 and x<=1:
	fx=x+2
else:
	fx=5*x+3 

print('x=%d,fx=%d'%(x,fx))