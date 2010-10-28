#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Game(object):
    def __init__(self, home, visitor, ruleset):
        self.home = home
        self.visitor = visitor
        self.ruleset = ruleset(self)

        self.score = [0, 0]
        self.time = 0.0
