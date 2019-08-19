"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

Date    : 2019-08-14 13:40:25
Author  : Younth Yang (8593009@qq.com)
"""
import math

class Point(object):
	"""docstring for Point"""
	def __init__(self, x = 0, y = 0):
		super(Point, self).__init__()
		self.x = x
		self.y = y
	
	def move_to(self, x, y):
		self.x = x
		self.y = y

	def move_by(self, dx, dy):
		self.x += dx
		self.y += dy

	def distance_to(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		return math.sqrt(dx ** 2 + dy ** 2)

	def __str__(self):
		return '(%s, %s)' % (str(self.x), str(self.y))

def main():
	point1 = Point(5, 9)
	print(point1)
	point1.move_to(4,20)
	print(point1)
	point2 = Point()
	print(point2)

	print(point1.distance_to(point2))

if __name__ == '__main__':
	main()

