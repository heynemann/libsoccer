#!/usr/bin/env python
#-*- coding:utf-8 -*-

class RuleSet(object):
    DEFENSE = 0
    OFFENSE = 1
    def __init__(self, game):
        self.game = game