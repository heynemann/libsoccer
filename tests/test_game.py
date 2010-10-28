#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.team import Team
from libsoccer.player import *
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

    def test_game_starting_position_comes_from_ruleset(self):
        assert self.game.position == self.game.ruleset.starting_position

    def test_game_starting_side_comes_from_ruleset(self):
        assert self.game.side == self.game.ruleset.starting_side

    #imagine all the people
    def test_game_starts_with_no_possession(self):
        assert not self.game.possession

    def test_after_game_start_some_team_has_possession(self):
        self.game.start()
        assert self.game.possession == self.team1 or \
               self.game.possession == self.team2

    def test_no_player_has_ball_before_game_began(self):
        assert not self.game.player_with_ball

    def test_proper_player_has_ball_after_game_start(self):
        self.game.start()
        assert self.game.player_with_ball
        assert self.game.player_with_ball.__class__ in [Midfielder, Striker]
