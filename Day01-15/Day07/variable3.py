"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:

Date    : 2019-08-08 14:57:21
Author  : Younth Yang (8593009@qq.com)
"""
import	sys

def main():
	list1 = [x for x in range(1,10)]
	print(list1)
	list2 = [x +y for x in '12' for y in 'ddd']
	print(list2)
	x=3
	print(3**2)
	f = [x ** 2 for x in range(1, 1000)]
	print(sys.getsizeof(f))  # 查看对象占用内存的字节数
	# print(f)

	f = (x ** 2 for x in range(1, 1000))
	print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
	print(f)
	for val in f:
		print(val)
	# for val in f:
		# print(val)


if __name__ == '__main__':
	main()

