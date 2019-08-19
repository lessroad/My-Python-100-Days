"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :奥特曼打小怪兽

Date    : 2019-08-15 15:28:35
Author  : Younth Yang (8593009@qq.com)
"""

from abc import abstractmethod, ABCMeta
from random import randrange, randint


class Fighter(object, metaclass=ABCMeta):
    """docstring for Fighter"""
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if self._hp > 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    """docstring for Ultraman"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other._hp -= randint(15, 25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other._hp -= injury

            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for x in others:
                if x.alive:
                    x._hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp


class Monster(Fighter):
    """docstring for Monster"""
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other._hp -= randint(10, 20)

    def __str__(self):
        return'~~~%s小怪兽~~~\n' % self._name + '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    for x in monsters:
        if x.alive:
            return True
    return False


def select_alive_one(monsters):
    num = len(monsters)
    while True:
        index = randrange(num)
        if monsters[index].alive:
            return monsters[index]


def display_info(ultraman, monsters):
    print(ultraman)
    for x in monsters:
        print(x, end='')


def main():
    u = Ultraman('奥特曼', 1000, 120)
    m1 = Monster('小怪兽1', 300)
    m2 = Monster('小怪兽2', 500)
    m3 = Monster('小怪兽3', 200)

    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill > 6:
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()
