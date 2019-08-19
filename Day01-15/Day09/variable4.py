"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :

Date    : 2019-08-15 15:16:40
Author  : Younth Yang (8593009@qq.com)
"""

import abc


class Pet(object, metaclass=abc.ABCMeta):
    """docstring for Pet"""

    def __init__(self, nickname):

        self._nickname = nickname

    @abc.abstractmethod
    def makevoice(self,):
        pass


class Dog(Pet):
    """docstring for dog"""

    def makevoice(self):
        print('%s:汪汪汪' % self._nickname)


class Cat(Pet):
    """docstring for Cat"""

    def makevoice(self):
        print('%s:喵喵喵' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('网球'), Dog('大黄')]
    for x in pets:
        x.makevoice()

if __name__ == '__main__':
    main()
