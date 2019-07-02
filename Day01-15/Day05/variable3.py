"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:百钱百鸡

Date    : 2019-07-02 12:50:08
Author  : Younth Yang (8593009@qq.com)
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))