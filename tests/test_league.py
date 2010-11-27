#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.league import League

class TestLeague(unittest.TestCase):

    def test_can_create_league(self):
        league = League(name="MY league",
                        average_skill=30)

        assert league.name == "MY league"
        assert league.average_skill == 30

    def test_can_generate_league(self):
        league = League.generate(name="My League",
                                 average_skill=50,
                                 number_of_starters=11,
                                 number_of_subs=9,
                                 number_of_teams=15)

        assert len(league.teams) == 15

    def test_can_get_league_unicode(self):
        league = League.generate(name="My League",
                                 average_skill=50,
                                 number_of_starters=11,
                                 number_of_subs=9,
                                 number_of_teams=15)

        league_str = unicode(league)
        print league_str

        assert "My League" in league_str
