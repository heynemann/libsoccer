#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Module responsible for representing a team
'''

from libsoccer.player import Player, GoalKeeper, Defender
from libsoccer.player import Wing, Midfielder, Striker

class Team(object):
    '''
    Model that represents a team with its starters and substitutes.
    '''
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
    def generate(cls,
                 name,
                 starters=None,
                 starter_skill=50,
                 substitutes=None,
                 substitutes_skill=35):
        '''
        Generates a team with the number of specified players
        and skills ranging around the specified skills.
        '''
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
                player = Player.generate(positions[position],
                                         current_number,
                                         starter_skill)
                generated_starters.append(player)
                current_number += 1

        for position, number_of_players in enumerate(substitutes):
            for player_index in range(number_of_players):
                player = Player.generate(positions[position],
                                         current_number,
                                         substitutes_skill)
                generated_substitutes.append(player)
                current_number += 1

        return Team(name, generated_starters, generated_substitutes)
