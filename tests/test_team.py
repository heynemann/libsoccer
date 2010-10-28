#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.team import Team

class TestTeam(unittest.TestCase):

    def test_can_create_team(self):
        team = Team('some team', ['player'], ['player'])
        assert team, "Can't create team"
        assert team.name == 'some team'
        assert team.starters
        assert team.substitutes

    def test_can_generate_team_with_defaults(self):
        team = Team.generate('Concha Dourada FC')

        assert team.__class__ == Team
        assert team.name == 'Concha Dourada FC'
        assert len(team.starters) == 11
        assert len(team.substitutes) == 7

    def test_generating_team_with_proper_values(self):
        team = Team.generate(
            name='Concha Dourada FC',
            starters=[1, 2, 2, 3, 3],
            substitutes=[1, 2, 1, 2, 2],
            starter_skill=50,
            substitutes_skill=35
        )

        assert len(team.starters) == 11
        assert len(team.substitutes) == 8

    def test_team_str(self):
        team = Team.generate('Concha Dourada FC')

        team_str = str(team)

        assert 'Concha Dourada FC' in team_str
        assert '\nStarter Players:\n\n' in team_str
        assert '\nSubstitutes:\n\n' in team_str
