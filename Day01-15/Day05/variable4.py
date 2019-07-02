"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:斐波拉契数列

Date    : 2019-07-02 13:00:08
Author  : Younth Yang (8593009@qq.com)
"""

a = 0
b = 1
for _ in range(200):
    a, b = b, a + b
    print(a, end=' ')