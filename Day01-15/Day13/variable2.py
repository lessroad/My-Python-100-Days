"""
-*- coding: utf-8 -*-
Project    :Python-100-Days

Name    :

Date    : 2019-08-27 19:23:32
Author  : Younth Yang (8593009@qq.com)
"""

from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid


def download_task(filename):
    print('启动下载进程,PID:%s' % getpid())
    print('开始下载%s' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成!耗时%d' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=['Python-100-Days'])
    p1.start()
    p2 = Process(target=download_task, args=['Python从入门到住院'])
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总耗时%.2f' % (end - start))

if __name__ == '__main__':
    main()
