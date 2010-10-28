#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random

from libsoccer.names import random_name
from libsoccer.player import Player, GoalKeeper, Defender, Wing, Midfielder, Striker

class Team(object):
    def __init__(self, name, starters, substitutes):
        self.name = name
        self.starters = starters
        self.substitutes = substitutes

    def __str__(self):
        text = [self.name,
                '\nStarter Players:\n\n']
        for player in self.starters:
            text.append(str(player))
            text.append('\n')
        text.append('\nSubstitutes:\n\n')
        for player in self.substitutes:
            text.append(str(player))
            text.append('\n')

        return u''.join(text)

    @classmethod
    def generate(cls, name, starters=None, starter_skill=50, substitutes=None, substitutes_skill=35):
        positions = [GoalKeeper, Defender, Wing, Midfielder, Striker]

        if not starters:
            starters = [1, 2, 2, 3, 3]

        if not substitutes:
            substitutes = [1, 2, 1, 2, 1]

        generated_starters = []
        generated_substitutes = []

        current_number = 1
        for position, number_of_players in enumerate(starters):
            for player_index in range(number_of_players):
                generated_starters.append(Player.generate(positions[position], current_number, starter_skill))
                current_number += 1

        for position, number_of_players in enumerate(substitutes):
            for player_index in range(number_of_players):
                generated_substitutes.append(Player.generate(positions[position], current_number, substitutes_skill))
                current_number += 1

        return Team(name, generated_starters, generated_substitutes)

