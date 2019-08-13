"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:计算指定的年月日是这一年的第几天

Date    : 2019-08-13 10:35:18
Author  : Younth Yang (8593009@qq.com)
"""

def is_leap_year(year):
	return (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0)

def which_day(year, month, date):
	total = 0
	days_of_month = [[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]][is_leap_year(year)]

	for x in range( month - 1):
		total += days_of_month[x]
	return total + date


def main():
	print(is_leap_year(2000))
	print(is_leap_year(2008))
	print(is_leap_year(2019))
	print(which_day(2019,8,13))


if __name__ == '__main__':
	main()