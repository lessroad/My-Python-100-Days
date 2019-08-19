"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :

Date    : 2019-08-15 10:14:29
Author  : Younth Yang (8593009@qq.com)
"""

import math

class Triangle(object):
	"""docstring for Triangle"""
	def __init__(self, a, b, c):
		super(Triangle, self).__init__()
		self._a = a
		self._b = b
		self._c = c

	@staticmethod
	def is_valid(a, b, c):
		return a + b > c and a + c > b and b + c > a

	def perimeter(self):
		return self._a + self._b + self._c

	def area(self):
		half = self.perimeter() / 2
		return math.sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def main():
	a, b,c = 3,4,5
	if Triangle.is_valid(a,b,c):
		t = Triangle(a,b,c)
		print(t.perimeter())
		print(t.area())

		print(Triangle.area(t))
	else:
		print('无法构成三角形')

if __name__ == '__main__':
	main()
