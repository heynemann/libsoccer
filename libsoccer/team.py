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

    @property
    def goalkeeper(self):
        return self.players_for(GoalKeeper)[0]

    @property
    def defenders(self):
        return self.players_for(Defender)

    @property
    def wings(self):
        return self.players_for(Wing)

    @property
    def midfielders(self):
        return self.players_for(Midfielder)

    @property
    def strikers(self):
        return self.players_for(Striker)

    def players_for(self, position):
        return [player for player in self.starters if player.__class__ == position]

    def __str__(self):
        return unicode(self)

    def __unicode__(self):
        text = [self.name,
                '\nStarter Players:\n\n']
        for player in self.starters:
            text.append(unicode(player))
            text.append('\n')
        text.append('\nSubstitutes:\n\n')
        for player in self.substitutes:
            text.append(unicode(player))
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
                player = positions[position].generate(current_number, starter_skill)
                generated_starters.append(player)
                current_number += 1

        for position, number_of_players in enumerate(substitutes):
            for player_index in range(number_of_players):
                player = positions[position].generate(current_number, substitutes_skill)
                generated_substitutes.append(player)
                current_number += 1

        return Team(name, generated_starters, generated_substitutes)

