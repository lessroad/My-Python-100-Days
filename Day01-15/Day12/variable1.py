"""
-*- coding: utf-8 -*-
Project    :Python-100-Days

Name    :验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0

Date    : 2019-08-22 13:22:25
Author  : Younth Yang (8593009@qq.com)
"""

import re

def main():
    username = input('请输入用户名:')
    qq = input('请输入qq号:')
    m1 = re.match(r'^[0-9a-zA-z]{6-20}$', username)
    if not m1:
        print('请输入正确的用户名')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('你输入的信息是有效的!')

if __name__ == '__main__':
    main()