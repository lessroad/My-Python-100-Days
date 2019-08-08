"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:摇骰子

Date    : 2019-07-02 15:23:01
Author  : Younth Yang (8593009@qq.com)
"""

from random import randint

def roll_dice(n=2):
	total = 0
	for x in range(n):
		total += randint(1,6)
	return total

print(roll_dice())
print(roll_dice(3))

def add(a=0, b=0, c=0):
	print("%d,%d,%d"%(a,b,c))
	return a + b + c

print (add(b=0,c=2,a=5))

def addarg(*args):
	total = 0
	for x in args:
		total += x
	return total
print(addarg(2,3,4,5,6,7))