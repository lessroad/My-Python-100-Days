"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:

Date    : 2019-08-08 14:23:14
Author  : Younth Yang (8593009@qq.com)
"""

def main():
	list1 = [1,2,4,7,9,45]
	print(list1)
	list2 = ['hello','world','4'] * 5
	print(list2)
	print(len(list1))
	print(list1[5])
	list1[2] = 5
	list1 += [9,2]
	print(list1)
	del list1[0]
	print(list2)
    # 清空列表元素
	list3 = sorted(list2)
	print(list3)
	print(list1.sort())



if __name__ == '__main__':
	main()
