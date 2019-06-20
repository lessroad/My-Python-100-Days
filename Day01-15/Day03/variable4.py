"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:掷骰子决定做什么事情

Date    : 2019-05-24 14:34:49
Author  : Younth Yang (8593009@qq.com)
"""

from random import randint

face = randint(1,6)
if face == 1:
    result = '唱首歌'
elif face == 2:
    result = '跳个舞'
elif face == 3:
    result = '学狗叫'
elif face == 4:
    result = '做俯卧撑'
elif face == 5:
    result = '念绕口令'
else:
    result = '讲冷笑话'
print(face,result)