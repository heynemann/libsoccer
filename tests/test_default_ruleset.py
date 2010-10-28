#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.player import *
from libsoccer.sets.base import RuleSet
from libsoccer.sets.default import DefaultRuleSet

class TestDefaultRuleSet(unittest.TestCase):

    def setUp(self):
        self.ruleset = DefaultRuleSet(game="game")

    def test_can_create_default_ruleset(self):
        assert self.ruleset
        assert self.ruleset.game == "game"

    def test_default_ruleset_positions(self):
        assert self.ruleset.positions
        assert len(self.ruleset.positions) == 10

    def test_default_ruleset_starting_position(self):
        assert self.ruleset.starting_position == 8

    def test_default_ruleset_starting_side(self):
        assert self.ruleset.starting_side == RuleSet.DEFENSE

    def test_default_ruleset_defense_positions(self):
        assert len(self.ruleset.defense_positions.keys()) == 10

        assert self.ruleset.defense_positions[0] == [Defender, Wing]
        assert self.ruleset.defense_positions[1] == [Defender, Wing]
        assert self.ruleset.defense_positions[2] == [Defender, Wing, Midfielder]
        assert self.ruleset.defense_positions[3] == [Defender, Wing, Midfielder]
        assert self.ruleset.defense_positions[4] == [Defender, Wing]
        assert self.ruleset.defense_positions[5] == [Defender, Wing]
        assert self.ruleset.defense_positions[6] == [Wing, Midfielder]
        assert self.ruleset.defense_positions[7] == [Midfielder, Striker]
        assert self.ruleset.defense_positions[8] == [Midfielder, Striker]
        assert self.ruleset.defense_positions[9] == [Wing, Midfielder]

    def test_default_ruleset_offense_positions(self):
        assert len(self.ruleset.offense_positions.keys()) == 10

        assert self.ruleset.offense_positions[0] == [Midfielder, Wing]
        assert self.ruleset.offense_positions[1] == [Midfielder, Wing, Striker]
        assert self.ruleset.offense_positions[2] == [Midfielder, Striker]
        assert self.ruleset.offense_positions[3] == [Striker]
        assert self.ruleset.offense_positions[4] == [Midfielder, Wing, Striker]
        assert self.ruleset.offense_positions[5] == [Midfielder, Wing]
        assert self.ruleset.offense_positions[6] == [Wing, Midfielder]
        assert self.ruleset.offense_positions[7] == [Midfielder, Striker]
        assert self.ruleset.offense_positions[8] == [Midfielder]
        assert self.ruleset.offense_positions[9] == [Wing, Midfielder]
