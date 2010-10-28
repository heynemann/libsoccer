#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''Module responsible for random actions'''

import random

def draw(options):
    '''Draws a random item among the given options'''
    return random.choice(options)

def d(sides):
    '''Rolls a dice with the given sides and returns a number'''
    return random.randint(1, sides)

def randint(min_number, max_number):
    '''Returns a random integer from min_number to max_number'''
    return random.randint(min_number, max_number)
