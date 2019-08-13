"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:设计一个函数返回给定文件名的后缀名

Date    : 2019-08-13 09:47:02
Author  : Younth Yang (8593009@qq.com)
"""

def get_suffix(filename, is_dot =False):
	index = filename.rfind('.')
	print(index)
	if 0 < index < len(filename) - 1:
		index = index if is_dot else index + 1
		print(index)
		return filename[index:]
	else:
		return ''

def main():
	print(get_suffix('1213dsfds.ddes.dsse',True))

if __name__ == '__main__':
	main()