"""
-*- coding: utf-8 -*-
Project	:Python-100-Days

Name    :

Date    : 2019-08-19 11:07:57
Author  : Younth Yang (8593009@qq.com)
"""

import random


class Card(object):
    """docstring for Card"""

    def __init__(self, suite, face):

        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """docstring for Poker"""

    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦' for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def is_has_next(self):
        return self._current < len(self._cards)


class Palyer(object):

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        self._cards_on_hand.sort(key=card_key)


def get_key(card):
    return (card.suite, card.face)


def main():
    p = Poker()
    p.shuffle()
    players = [Palyer('张三'), Palyer('李四'), Palyer('王二麻子'), Palyer('小淘气')]

    for x in range(13):
        for y in players:
            y.get(p.next)
    for y in players:
        print(y.name + ':', end=' ')
        y.arrange(get_key)
        print(y.cards_on_hand)

if __name__ == '__main__':
    main()
