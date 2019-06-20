"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:英制单位英寸和公制单位厘米互换

Date    : 2019-05-24 14:31:13
Author  : Younth Yang (8593009@qq.com)
"""

value = float(input('请输入长度:'))
unit = input('请输入单位:')
if unit=='in':
	print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit =='cm':
	print('%f厘米 = %f英寸' % (value, value / 2.54))
else :
	print('请输入正确的单位')