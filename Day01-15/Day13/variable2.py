from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid


def download_task(filename):
    print('pid:%s' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(1, 3)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('1'))
    p1.start()
    p2 = Process(target=download_task, args=('2'))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('耗时%d秒' % (end-start))


if __name__ == "__main__":
    main()
