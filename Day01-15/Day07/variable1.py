"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:字符串

Date    : 2019-08-08 13:30:40
Author  : Younth Yang (8593009@qq.com)
"""

def main():
	str1 = 'hello, world!'
	print(len(str1))
	print(str1.capitalize())
	print(str1.upper())
	print(str1.find('hedllo'))
	print(str1.startswith('hello'))
	print(str1.endswith('hello'))
	print(str1.center(14,'*'))
	print(str1.rjust(14,'*'))
	print(str1.ljust(16,'*'))

	str2='abcd12346'
	print(str2[2])
	print(str2[-3:-1])
	print(str2.isalnum())
	print(str2.isalpha())
	print(str2.isdigit())
	p

if __name__ == '__main__':
	main()

