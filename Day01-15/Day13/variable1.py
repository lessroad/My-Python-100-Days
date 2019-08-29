"""
-*- coding: utf-8 -*-
Project    :Python-100-Days

Name    :

Date    : 2019-08-27 17:04:50
Author  : Younth Yang (8593009@qq.com)
"""

from random import randint
from time import sleep, time


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成,耗时%s' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python-100-Days')
    download_task('Python从入门到入院')
    end = time()
    print('总共好吃%.2f秒' % (end - start))

if __name__ == '__main__':
    main()
