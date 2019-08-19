"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :

Date    : 2019-08-15 09:02:26
Author  : Younth Yang (8593009@qq.com)
"""


class Persion(object):
    """docstring for Persion"""

    __slots__ = ('_name', '_age', '_gender', '_phone')

    def __init__(self, name, age, phone=''):
        super(Persion, self).__init__()
        self._name = name
        self._age = age
        self._phone = phone

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def paly(self):
        print('%s正在愉快的玩耍' % (self._name))

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Persion):
    """docstring for Student"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))


class Teacher(Persion):
    """docstring for Teacher"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def titel(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在教%s' % (self._name, self._title, course))


def main():
    p1 = Student('张三', 20, '大学')
    p1.study('Python')
    p1.age = 14
    p1.study('C#')
    t1 = Teacher('李四', 50, '教授')
    t1.teach('golang')
    t1.watch_av()

if __name__ == '__main__':
    main()
