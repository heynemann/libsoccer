#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libsoccer.sets.base import RuleSet

class DefaultRuleSet(RuleSet):
    def __init__(self):
        self.positions = range(10)