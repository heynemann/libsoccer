#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.team import Team
from libsoccer.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.team1 = Team.generate(name='Team1')
        self.team2 = Team.generate(name='Team2')

    def test_can_create_game(self):
        game = Game(home=self.team1, visitor=self.team2)
        assert game

    def test_game_keeps_teams(self):
        game = Game(home=self.team1, visitor=self.team2)
        assert game.home == self.team1
        assert game.visitor == self.team2
