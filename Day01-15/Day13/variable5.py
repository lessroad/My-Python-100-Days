from random import randint
from threading import Thread
from time import time, sleep

class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def  run(self):
        print('开始下载%s' % self._filename)
        time_to_download = randint(3,7)
        sleep(time_to_download)
        print('下载完成%s，耗时%d' % (self._filename, time_to_download))

def  main():
    start = time()
    d1 = DownloadTask('1')
    d1.start()
    d2 = DownloadTask('2')
    d2.start()
    d1.join()
    d2.join()
    end = time()
    print('总耗时%d' % (end - start))

if __name__ == "__main__":
    main()