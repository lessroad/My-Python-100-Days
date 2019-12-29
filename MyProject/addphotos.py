import os
import shutil
import hashlib
import exifread
import re
import time
import configparser

fromdir = ""
todir = ""
extinfo = ""
md5file = ""

def del_empty():
    for root, dirs, files in os.walk(fromdir):
        if not os.listdir(root):
            os.rmdir(root)

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

def get_config():
    global fromdir, todir,extinfo,md5file
    conf = configparser.ConfigParser()
    # 读ini文件
    conf.read('addphotos.ini', encoding="utf-8")  # python3
    fromdir =  conf.get("from","path")
    todir =  conf.get("to","path")
    extinfo = conf.get("from","ext")
    md5file = os.path.join(todir,conf.get("to","md5"))

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

def move_file():
    d,a,e=0,0,0
    for i, j, k in os.walk(fromdir):
        for p in k:
            ext = os.path.splitext(p)[1]
            d = d + 1
            filefrompath = os.path.join(i,p)
            is_move = False
            filetopath = ""
            if ext.lower() in extinfo:
                md5 = get_file_md5(filefrompath)
                with open(md5file, 'r') as f:
                    if md5 in f.read():
                        f = open(os.path.join(fromdir,"re.txt"), 'a')
                        f.write(md5 + ' ' +filefrompath+'\n')
                        f.close()
                        continue
                a=a+1
                if ext.lower() in ['.png','.jpeg','.jpg']:
                    with open(filefrompath, 'rb') as f:
                        tags = exifread.process_file(f)
                        for tag, value in tags.items():
                            if re.match('EXIF DateTimeOriginal', tag):
                                filetopath = get_new_filename(ext, value)
                                is_move = True
                if not is_move:
                    fileinfo = os.stat(filefrompath)
                    filetopath = get_new_filename(ext, time.strftime(
                        "%Y:%m:%d %H:%M:%S", time.localtime(fileinfo.st_mtime)))
                    is_move = True
            if is_move:
                e = e+1                
                try:
                    shutil.move(filefrompath, filetopath)
                    f = open(md5file, 'a')
                    f.write(md5+' '+filetopath+'\n')
                    f.close()
                except:
                    print(filefrompath)
        print(e,a,d,filefrompath,filetopath)

def main():
    get_config()
    move_file()
    del_empty()

if __name__ == "__main__":
    main()