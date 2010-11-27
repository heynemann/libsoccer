#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Module responsible for representing a League
'''

from libsoccer.team import Team

class League(object):
    '''
    Model that represents a League of teams. 
    '''
    def __init__(self, name, average_skill):
        self.name = name
        self.average_skill = average_skill
        self.teams = []

    def __unicode__(self):
        text = [self.name,
                ' (avg. skill: %s)' % self.average_skill,
                '\nTeams in League:\n\n']
        for team in self.teams:
            text.append(unicode(team))
            text.append('\n')

        return u''.join(text)

    @classmethod
    def generate(cls,
                 name,
                 average_skill,
                 number_of_starters,
                 number_of_subs,
                 number_of_teams,
                 team_names):
        '''
        Generates a league with the number of teams specified
        with the average skill.
        '''
        league = League(name, average_skill)

        for i in range(number_of_teams):
            team = Team.generate(
