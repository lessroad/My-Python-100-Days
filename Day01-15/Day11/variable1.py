"""
-*- coding: utf-8 -*-
Project    :Python-100-Days

Name    :

Date    : 2019-08-21 10:58:28
Author  : Younth Yang (8593009@qq.com)
"""


def main():

    try:
        with open('test.txt', 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end='')

        print()

    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main()
