"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name	:

Date    : 2019-08-08 15:22:20
Author  : Younth Yang (8593009@qq.com)
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)
        
if __name__ == '__main__':
	main()