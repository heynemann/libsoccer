#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.sets.base import RuleSet
from libsoccer.sets.default import DefaultRuleSet

class TestDefaultRuleSet(unittest.TestCase):

    def setUp(self):
        self.rule_set = DefaultRuleSet(game="game")

    def test_can_create_default_ruleset(self):
        assert self.rule_set
        assert self.rule_set.game == "game"

    def test_default_ruleset_positions(self):
        assert self.rule_set.positions
        assert len(self.rule_set.positions) == 10

    def test_default_ruleset_starting_position(self):
        assert self.rule_set.starting_position == 8

    def test_default_ruleset_starting_side(self):
        assert self.rule_set.starting_side == RuleSet.DEFENSE