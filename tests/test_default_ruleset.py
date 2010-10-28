#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.sets.default import DefaultRuleSet

class TestDefaultRuleSet(unittest.TestCase):

    def setUp(self):
        self.rule_set = DefaultRuleSet()

    def test_can_create_default_ruleset(self):
        assert self.rule_set

    def test_default_ruleset_positions(self):
        assert self.rule_set.positions
        assert len(self.rule_set.positions) == 10