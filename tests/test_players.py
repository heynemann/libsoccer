#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.players import Player
from libsoccer.players import GoalKeeper, Defender, Wing, Midfielder, Striker

class TestPlayer(unittest.TestCase):

    def test_can_get_player_string_representation(self):
        player = Player(name="Test Player",
                        number=10,
                        speed=75,
                        agility=45,
                        stamina=90,
                        offense=48,
                        defense=25)
        representation = str(player).strip()

        assert u"[Player] 10 - Test Player with stats:" in representation
        assert u"speed(key):75" in representation
        assert u"agility(key):45" in representation
        assert u"stamina(key):90" in representation
        assert u"offense:48" in representation
        assert u"defense:25" in representation

    def test_can_create_player(self):
        player = Player(name="Test Player",
                        number=10,
                        speed=75,
                        agility=45,
                        stamina=90,
                        offense=48,
                        defense=25)
        assert player, "Can't create player"

    def test_player_constructor(self):
        player = Player(name="Test Player",
                        number=10,
                        speed=75,
                        agility=45,
                        stamina=90,
                        offense=48,
                        defense=25)

        assert player.name == "Test Player"
        assert player.number == 10
        assert player.speed == 75
        assert player.agility == 45
        assert player.stamina == 90
        assert player.offense == 48
        assert player.defense == 25

    def test_can_create_random_goalie(self):
        player = GoalKeeper.generate(number=1, median=50)

        assert player.__class__ == GoalKeeper, player.__class__
        assert player.name
        assert player.number == 1

    def test_can_create_random_goalie_with_proper_rates(self):
        offset_size = 2
        median = 50
        min_val = median - (7 * offset_size)
        max_val = median + (7 * offset_size)

        player = GoalKeeper.generate(number=1, median=median, offset_size=offset_size)

        assert player.speed >= min_val and player.speed <= max_val, player
        assert player.agility >= min_val and player.agility <= max_val, player
        assert player.stamina >= min_val and player.stamina <= max_val, player
        assert player.offense <= max_val, player
        assert player.defense >= min_val and player.defense <= max_val, player
        assert player.anticipation >= min_val and player.anticipation <= max_val, player
        assert player.positioning >= min_val and player.positioning <= max_val, player
        assert player.jumping >= min_val and player.jumping <= max_val, player

    def test_can_create_random_defender_with_proper_rates(self):
        offset_size = 2
        median = 50
        min_val = median - (7 * offset_size)
        max_val = median + (7 * offset_size)

        player = Defender.generate(number=4, median=median, offset_size=offset_size)

        assert player.speed >= min_val and player.speed <= max_val, player
        assert player.agility >= min_val and player.agility <= max_val, player
        assert player.stamina >= min_val and player.stamina <= max_val, player
        assert player.offense <= max_val, player
        assert player.defense >= min_val and player.defense <= max_val, player
        assert player.marking >= min_val and player.marking <= max_val, player
        assert player.movement >= min_val and player.movement <= max_val, player
        assert player.stealing >= min_val and player.stealing <= max_val, player

    def test_can_create_random_wing_with_proper_rates(self):
        offset_size = 2
        median = 50
        min_val = median - (7 * offset_size)
        max_val = median + (7 * offset_size)

        player = Wing.generate(number=6, median=median, offset_size=offset_size)

        assert player.speed >= min_val and player.speed <= max_val, player
        assert player.agility <= max_val, player
        assert player.stamina >= min_val and player.stamina <= max_val, player
        assert player.offense >= min_val and player.offense <= max_val, player
        assert player.defense >= min_val and player.defense <= max_val, player
        assert player.progression >= min_val and player.progression <= max_val, player
        assert player.crossing >= min_val and player.crossing <= max_val, player
        assert player.dribbling >= min_val and player.dribbling <= max_val, player

    def test_can_create_random_midfielder_with_proper_rates(self):
        offset_size = 2
        median = 50
        min_val = median - (7 * offset_size)
        max_val = median + (7 * offset_size)

        player = Midfielder.generate(number=6, median=median, offset_size=offset_size)

        assert player.speed >= min_val and player.speed <= max_val, player
        assert player.agility <= max_val, player
        assert player.stamina >= min_val and player.stamina <= max_val, player
        assert player.offense >= min_val and player.offense <= max_val, player
        assert player.defense >= min_val and player.defense <= max_val, player
        assert player.marking >= min_val and player.marking <= max_val, player
        assert player.passing >= min_val and player.passing <= max_val, player
        assert player.arming >= min_val and player.arming <= max_val, player

    def test_can_create_random_striker_with_proper_rates(self):
        offset_size = 2
        median = 50
        min_val = median - (7 * offset_size)
        max_val = median + (7 * offset_size)

        player = Striker.generate(number=11, median=median, offset_size=offset_size)

        assert player.speed >= min_val and player.speed <= max_val, player
        assert player.agility >= min_val and player.agility <= max_val, player
        assert player.stamina >= min_val and player.stamina <= max_val, player
        assert player.offense >= min_val and player.offense <= max_val, player
        assert player.defense <= max_val, player
        assert player.kicking >= min_val and player.kicking <= max_val, player
        assert player.heading >= min_val and player.heading <= max_val, player
        assert player.dribbling >= min_val and player.dribbling <= max_val, player

class TestGoalKeeper(unittest.TestCase):

    def test_can_create_player(self):
        player = GoalKeeper(name="Test Player",
                            number=10,
                            speed=75,
                            agility=45,
                            stamina=90,
                            offense=48,
                            defense=25,
                            anticipation=72,
                            positioning=57,
                            jumping=88)
        assert player, "Can't create player"

    def test_player_ctor(self):
        player = GoalKeeper(name="Test Player",
                            number=10,
                            speed=75,
                            agility=45,
                            stamina=90,
                            offense=48,
                            defense=25,
                            anticipation=72,
                            positioning=57,
                            jumping=88)

        assert player.name == "Test Player"
        assert player.anticipation == 72
        assert player.positioning == 57
        assert player.jumping == 88

class TestDefender(unittest.TestCase):

    def test_can_create_player(self):
        player = Defender(name="Test Player",
                            number=10,
                            speed=75,
                            agility=45,
                            stamina=90,
                            offense=48,
                            defense=25,
                            movement=72,
                            marking=57,
                            stealing=88)
        assert player, "Can't create player"

    def test_player_ctor(self):
        player = Defender(name="Test Player",
                            number=10,
                            speed=75,
                            agility=45,
                            stamina=90,
                            offense=48,
                            defense=25,
                            movement=72,
                            marking=57,
                            stealing=88)

        assert player.name == "Test Player"
        assert player.movement == 72
        assert player.marking == 57
        assert player.stealing == 88

class TestWing(unittest.TestCase):

    def test_can_create_wing(self):
        wing = Wing(name="Test Player",
                    number=10,
                    speed=75,
                    agility=45,
                    stamina=90,
                    offense=48,
                    defense=25,
                    progression=72,
                    crossing=57,
                    dribbling=88)
        assert wing, "Can't create wing"

    def test_wing_ctor(self):
        wing = Wing(name="Test Player",
                    number=10,
                    speed=75,
                    agility=45,
                    stamina=90,
                    offense=48,
                    defense=25,
                    progression=72,
                    crossing=57,
                    dribbling=88)

        assert wing.name == "Test Player"
        assert wing.progression == 72
        assert wing.crossing == 57
        assert wing.dribbling == 88

class TestMidfielder(unittest.TestCase):

    def test_can_create_midfielder(self):
        mid = Midfielder(name="Test Player",
                         number=10,
                         speed=75,
                         agility=45,
                         stamina=90,
                         offense=48,
                         defense=25,
                         marking=72,
                         passing=57,
                         arming=88)
        assert mid, "Can't create midfielder"

    def test_midfielder_ctor(self):
        mid = Midfielder(name="Test Player",
                         number=10,
                         speed=75,
                         agility=45,
                         stamina=90,
                         offense=48,
                         defense=25,
                         marking=72,
                         passing=57,
                         arming=88)

        assert mid.name == "Test Player"
        assert mid.marking == 72
        assert mid.passing == 57
        assert mid.arming == 88

class TestStriker(unittest.TestCase):

    def test_can_create_striker(self):
        striker = Striker(name="Test Player",
                          number=10,
                          speed=75,
                          agility=45,
                          stamina=90,
                          offense=48,
                          defense=25,
                          dribbling=72,
                          kicking=57,
                          heading=88)
        assert striker, "Can't create striker"

    def test_midfielder_ctor(self):
        striker = Striker(name="Test Player",
                          number=10,
                          speed=75,
                          agility=45,
                          stamina=90,
                          offense=48,
                          defense=25,
                          dribbling=72,
                          kicking=57,
                          heading=88)

        assert striker.name == "Test Player"
        assert striker.dribbling == 72
        assert striker.kicking == 57
        assert striker.heading == 88
