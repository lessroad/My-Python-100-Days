"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :

Date    : 2019-08-14 13:06:35
Author  : Younth Yang (8593009@qq.com)
"""

class Test:
	"""docstring for Test"""
	def __init__(self, foo):
		self.__fooo = foo

	def __bar(self):
		print(self.__fooo)
		print('__bar')

def main():
	test = Test('hello')
	# test.__bar()

	# print(test.__foo)

	test._Test__bar()
	print(test._Test__fooo)

if __name__ == '__main__':
	main()
		