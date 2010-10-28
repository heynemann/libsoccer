#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libsoccer.dice import draw
from libsoccer.sets.base import RuleSet
from libsoccer.player import GoalKeeper, Defender, Wing
from libsoccer.player import Midfielder, Striker

class DefaultRuleSet(RuleSet):
    def __init__(self, game):
        super(DefaultRuleSet, self).__init__(game)
        self.positions = range(10)
        self.starting_side = RuleSet.DEFENSE
        self.starting_position = 8

    @property
    def defense_positions(self):
        return {
            0: [Defender, Wing],
            1: [Defender, Wing],
            2: [Defender, Wing, Midfielder],
            3: [Defender, Wing, Midfielder],
            4: [Defender, Wing],
            5: [Defender, Wing],
            6: [Wing, Midfielder],
            7: [Midfielder, Striker],
            8: [Midfielder, Striker],
            9: [Wing, Midfielder]
        }

    @property
    def offense_positions(self):
        return {
            0: [Midfielder, Wing],
            1: [Midfielder, Wing, Striker],
            2: [Midfielder, Striker],
            3: [Striker],
            4: [Midfielder, Wing, Striker],
            5: [Midfielder, Wing],
            6: [Wing, Midfielder],
            7: [Midfielder, Striker],
            8: [Midfielder],
            9: [Wing, Midfielder]
        }

    def pick_player(self, position, side):
        collection = side == RuleSet.DEFENSE and self.defense_positions or self.offense_positions

        position_class = draw(collection[position])

        return draw(self.game.possession.players_for(position_class))
