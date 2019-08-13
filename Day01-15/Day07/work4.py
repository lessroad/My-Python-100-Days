"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:设计一个函数返回传入的列表中最大和第二大的元素的值

Date    : 2019-08-13 10:12:42
Author  : Younth Yang (8593009@qq.com)
"""
def max2(x):
	(m1,m2) = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])

	for y in range(2,len(x)):
		if x[y] > m1:
			m2 = m1
			m1 = x[y]
		elif x[y] > m2:
			m2 = x[y]
	return m1, m2

def main():
	print(max2([1,2,3,1,4,51,5,12,5,321,5,21,421,6,555]))

if __name__ == '__main__':
	main()