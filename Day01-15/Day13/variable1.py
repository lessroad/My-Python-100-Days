from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(1, 3)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('1')
    download_task('2')
    end = time()
    print('耗时%d' % (end-start))


if __name__ == "__main__":
    main()
