"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :

Date    : 2019-08-14 12:45:33
Author  : Younth Yang (8593009@qq.com)
"""

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def study(self, course_name):
		print('%s正在学习%s'%(self.name, course_name))

	def watch_movie(self):
		if self.age < 18:
			print('%s只能看<熊出没>.'%(self.name))
		else:
			print('%s正在看岛国爱情大电影.'%(self.name))


def main():
	stu1 = Student('张三', 20)
	stu1.study('Python')
	stu1.watch_movie()

	stu2 = Student('李四', 16)
	stu2.study('C#')
	stu2.watch_movie()

if __name__ == '__main__':
	main()