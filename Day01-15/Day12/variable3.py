"""
-*- coding: utf-8 -*-
Project    :Python-100-Days

Name    :替换字符串中的不良内容

Date    : 2019-08-22 13:54:29
Author  : Younth Yang (8593009@qq.com)
"""

import re

def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


if __name__ == '__main__':
    main()