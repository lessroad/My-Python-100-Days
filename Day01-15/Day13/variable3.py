"""
-*- coding: utf-8 -*-
Project    :Python-100-Days

Name    :

Date    : 2019-08-27 19:41:40
Author  : Younth Yang (8593009@qq.com)
"""

from random import randint
from time import time, sleep
from threading import Thread



def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Ping',))
    t1.start()
    t2 = Thread(target=download, args=('Pong',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗时%.2f' % (end - start))

if __name__ == '__main__':
    main()
