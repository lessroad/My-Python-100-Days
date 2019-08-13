"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :打印杨辉三角

Date    : 2019-08-13 12:17:07
Author  : Younth Yang (8593009@qq.com)
"""

def main():
    num=int(input("请输入打印的行数:"))
    yh = [[]] * num
    print(yh)
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

if __name__ == '__main__':
	main()