#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.dice import draw, d, randint

class TestTeam(unittest.TestCase):
    def test_draw(self):
        items = [1,2,3,4]

        drawn = draw(items)

        assert drawn in items

def test_number():
    for i in range(1, 10):
        for j in range(11, 20):
            yield check_number, i, j

def check_number(min_number, max_number):
    generated = randint(min_number, max_number)
    assert generated >= min_number and generated <= max_number

def test_dices():
    for i in range(1, 101):
        yield check_dice, i

def check_dice(number):
    generated = d(number)
    assert generated >= 1 and generated <= number