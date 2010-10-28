#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libsoccer.dice import draw

class Game(object):
    def __init__(self, home, visitor, ruleset):
        self.home = home
        self.visitor = visitor
        self.ruleset = ruleset(self)

        self.score = [0, 0]
        self.time = 0.0
        self.position = self.ruleset.starting_position
        self.side = self.ruleset.starting_side
        self.possession = None
        self.player_with_ball = None

    def start(self):
        self.possession = draw([self.home, self.visitor])
        self.player_with_ball = self.ruleset.pick_player(self.position, self.side)