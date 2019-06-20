"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:用户什么验证

Date    : 2019-05-24 14:21:56
Author  : Younth Yang (8593009@qq.com)
"""

#import getpass

username = input('请输入用户名:')
password = input('请输入密码:')
#password = getpass.getpass('请输入密码:')

if username=='admin' and password == 'admin':
	print('验证正确!')
else:
	print('用户名或密码错误!')