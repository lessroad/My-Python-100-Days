"""
-*- coding: utf-8 -*-
Project    :Python-100-Days

Name    :

Date    : 2019-08-21 11:46:37
Author  : Younth Yang (8593009@qq.com)
"""

import json


def main():
    myjson = {
        "name": "骆昊",
        "age": 38,
        "qq": 957658,
        "friends": ["王大锤", "白元芳"],
        "cars": [
            {"brand": "BYD", "max_speed": 180},
            {"brand": "Audi", "max_speed": 280},
            {"brand": "Benz", "max_speed": 320}
        ]
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(myjson, f)

    with open('data.json', 'r', encoding='utf-8') as g:

        j = json.loads(g.read())
        print(j)
        print(j['friends'])
        for x in j['friends']:
            print(x)

    print('保存数据完成!')

if __name__ == '__main__':
    main()
