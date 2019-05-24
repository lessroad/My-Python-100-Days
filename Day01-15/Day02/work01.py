"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:输入园的半径计算周长和面积

Date    : 2019-05-24 12:01:39
Author  : Younth Yang (8593009@qq.com)
"""

import math

r=float(input('请输入圆的半径:'))
d=2*math.pi*r
m=math.pi*r*r

print('半径为%.2f的圆的周长为%.2f,面积为%.2f'%(r,d,m))