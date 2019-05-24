# Python-100-Days

# Work02  将华氏温度转换为摄氏温度
# F = 1.8C + 32

# -*- coding: utf-8 -*-
# Date    : 2019-05-16 15:08:46
# Author  : Younth Yang (8593009@qq.com)

f=float(input('请输入华氏温度:'))

c=(f-32)/1.8

print('%.1f的华氏温度=%.1f的摄氏温度'%(f,c))