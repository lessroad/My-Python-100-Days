import os
import shutil
import hashlib
import exifread
import re
import time


def get_file_md5(filepath):
    # 获取文件的md5
    if not os.path.isfile(filepath):
        return
    myhash = hashlib.md5()
    f = open(filepath, "rb")
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def get_all_ext(filepath):
    for i, j, k in os.walk(filepath):
        for p in k:
            with open(filepath + r'\ext.txt', 'r') as f:
                extinfo = os.path.splitext(p)[1]
                if extinfo not in f.read():
                    f = open(filepath + r'\ext.txt', 'a')
                    f.write(extinfo+'\n')
                    f.close()


def get_md5_movere(filepath):
    d, a = 0, 0
    for i, j, k in os.walk(filepath):
        for p in k:
            md5 = get_file_md5(r"%s\%s" % (i, p))
            with open(r'E:\照片\md5.txt', 'r') as f:
                if md5 not in f.read():
                    f = open(r'E:\照片\md5.txt', 'a')
                    f.write(md5 + r" %s\%s" % (i, p)+'\n')
                    f.close()
                else:
                    a = a+1
                    shutil.move(r"%s\%s" % (i, p), ('E:\\重复照片\\'+md5 + os.path.splitext(p)[1]))

            d = d+1
            print(d, a)


def get_new_filename(ext, datetime):
    timeArray = time.strptime(str(datetime).replace(
        '下午', '').replace('上午', ''), "%Y:%m:%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    path = ("E:\\照片\\%s\\%s" % (timeArray.tm_year, timeArray.tm_mon))
    if not os.path.exists(path):
        os.makedirs(path)
    new_filename = ("%s\\%s%s" %
                    (path, time.strftime("%Y-%m-%d %H%M%S", timeArray), ext))

    while os.path.exists(new_filename):
        timeStamp = timeStamp + 1
        new_filename = ("%s\\%s%s" % (path, time.strftime(
            "%Y-%m-%d %H%M%S", time.localtime(timeStamp)), ext))
    return new_filename


def classify(filepath):
    """整理包含拍摄信息的照片"""
    d, e, a = 0, 0, 0
    for i, j, k in os.walk(filepath):
        for p in k:
            ext = os.path.splitext(p)[1]
            d = d + 1
            path = r"%s\%s" % (i, p)
            is_move = False
            new_file = ""
            if ext.lower() in ['.jpg', '.jpeg', '.png', '.mpg', '.mov', '.mp4', '.3gp', '.m4v', '.avi']:
                a = a + 1
                try:
                    with open(path, 'rb') as f:
                        tags = exifread.process_file(f)
                        for tag, value in tags.items():
                            if re.match('EXIF DateTimeOriginal', tag):
                                new_file = get_new_filename(ext, value)
                                is_move = True
                    if not is_move:
                        fileinfo = os.stat(path)
                        new_file = get_new_filename(ext, time.strftime(
                            "%Y:%m:%d %H:%M:%S", time.localtime(fileinfo.st_mtime)))
                        is_move = True
                except:
                    print(path)
                    continue
            if is_move:
                e = e+1
                shutil.move(path, new_file)

            print("%d/%d/%d" % (e, a, d))


def del_empty(dir_path):
    for root, dirs, files in os.walk(dir_path):
        if not os.listdir(root):
            os.rmdir(root)


def main():

    filepath = r"E:\照片"
    # classify(filepath)
    # get_all_ext(filepath)
    # del_empty(filepath)
    get_md5_movere(filepath)


if __name__ == "__main__":
    main()
