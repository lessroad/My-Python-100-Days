"""
-*- coding: utf-8 -*-
Project    :Python-100-Days

Name    :复制图片

Date    : 2019-08-21 11:36:50
Author  : Younth Yang (8593009@qq.com)
"""

def main():
    try:
        with open('vh.jpg', 'rb') as f1:
            data = f1.read()
            print(type(data))

        with open('vh1.jpg', 'wb') as f2:
            f2.write(data)
    except IOError as e:
        print('文件读写错误')
        print(e)

if __name__ == '__main__':
    main()