#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.team import Team
from libsoccer.game import Game
from libsoccer.sets.default import DefaultRuleSet

class TestGame(unittest.TestCase):
    def setUp(self):
        self.team1 = Team.generate(name='Team1')
        self.team2 = Team.generate(name='Team2')
        self.game = Game(home=self.team1, visitor=self.team2, ruleset=DefaultRuleSet)

    def test_can_create_game(self):
        assert self.game

    def test_game_keeps_teams(self):
        assert self.game.home == self.team1
        assert self.game.visitor == self.team2

    def test_game_starts_with_proper_score(self):
        assert self.game.score == [0, 0]

    def test_game_starts_with_proper_time(self):
        assert self.game.time == 0.0

    def test_game_creates_ruleset_instance(self):
        assert self.game.ruleset
        assert self.game.ruleset.__class__ == DefaultRuleSet