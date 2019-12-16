from random import randint
from threading import Thread
from time import sleep ,time
from os import getpid

def  download_task(string):
    print('进程：%s' % getpid())
    print('开始下载%s' % string)
    sleep_time = randint(3,7)
    sleep(sleep_time)
    print('下载完成%s,耗时%d' % (string, sleep_time))

def main():
    start = time()
    t1 = Thread(target = download_task, args = ('111',))
    t1.start()
    t2 = Thread(target = download_task, args = ('222',))
    t2.start()

    t1.join()
    t2.join()
    end = time()
    print('总耗时%s'% (end-start))

if __name__ == "__main__":
    main()