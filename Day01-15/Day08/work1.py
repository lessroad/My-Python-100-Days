"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :定义一个类描述数字时钟

Date    : 2019-08-14 13:22:30
Author  : Younth Yang (8593009@qq.com)
"""

import time

class Clock(object):
	"""数字时钟"""
	def __init__(self, hour = 0, minute = 0, second = 0):
		self._hour = hour
		self._minute = minute
		self._second = second

	def run(self):
		self._second += 1
		if self._second == 60:
			self._minute += 1
			self._second = 0
			if self._minute == 60:
				self._hour += 1
				self._minute = 0
				if self_hour == 24:
					self._hour = 0

	def show(self):
		return '%02d:%02d:%02d'%(self._hour,self._minute,self._second)

def main():
	clock = Clock(12,39,58)
	while True:
		print(clock.show())
		time.sleep(1)
		clock.run()

if __name__ == '__main__':
	main()