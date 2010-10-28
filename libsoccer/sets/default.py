#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libsoccer.sets.base import RuleSet

class DefaultRuleSet(RuleSet):
    def __init__(self, game):
        super(DefaultRuleSet, self).__init__(game)
        self.positions = range(10)