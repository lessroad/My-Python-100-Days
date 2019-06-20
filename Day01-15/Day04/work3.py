"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:打印各种三角形图案

Date    : 2019-06-20 15:52:24
Author  : Younth Yang (8593009@qq.com)
"""

row=int(input('请输入行数'))
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()