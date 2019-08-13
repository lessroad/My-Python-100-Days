"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :双色球选号

Date    : 2019-08-13 15:59:58
Author  : Younth Yang (8593009@qq.com)
"""

import random

def random_select():
	red_balls = [x for x in range(1,34)]
	select_red_balls = random.sample(red_balls, 6)
	select_red_balls.sort()
	select_red_balls.append(random.randint(1,16))
	return select_red_balls

def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()

def main():
	print(display(random_select()))
	
if __name__ == '__main__':
	main()