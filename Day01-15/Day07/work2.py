"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:

Date    : 2019-08-08 17:15:04
Author  : Younth Yang (8593009@qq.com)
"""
import random

def get_code(code_len=4):
	"""
	获取指定长度验证码
	:param code_len: 验证码的长度(默认4个字符)

	:return: 由大小写英文字母和数字构成的随机验证码

	"""
	str='1234567890qwertyuiopasdfghjklzxcvnm'
	code = ''
	for x in range(code_len):
		code += str[random.randint(0,len(str) - 1)]

	return code

def main():
	print(get_code(6))

if __name__ == '__main__':
	main()