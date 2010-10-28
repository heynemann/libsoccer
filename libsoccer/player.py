#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Goleiro-Goalkeeper
# Zagueiro- Center Back
# Lateral direito;Lateral Esquerdo Jogando atrás - Full Back
# Lateral Direito, Lateral Esquerdo Ofensivos - Wing Back
# Libero é Libero mesmo
# Volante - Defensive Midfielder
# Ala - Side Medfielder
# Meias - Attacking Midfielder
# Atacante - Strikers
# Centroavante - Centre forward
# Tecnico - Coach

import random

from libsoccer.names import random_name

class Player(object):
    attributes = ('speed', 'agility', 'stamina', 'offense', 'defense')

    def __init__(self, name, number, speed, agility, stamina, offense, defense):
        self.name = name
        self.number = number
        self.speed = speed
        self.agility = agility
        self.stamina = stamina
        self.offense = offense
        self.defense = defense

    def __str__(self):
        text = ['[',
                self.__class__.__name__,
                '] ',
                str(self.number),
                ' - ',
                self.name,
                ' with stats:\n\t']

        for index in range(len(self.attributes)):
            attribute = self.__class__.attributes[index]
            text.append(attribute)
            if index < 3:
                text.append('(key)')
            text.append(':')
            text.append(str(getattr(self, attribute)))
            text.append('\n\t')

        return ''.join(text)

    @classmethod
    def generate(cls, number, median=50, offset_size=2):
        attributes = {
            'name': "%s %s" % random_name(),
            'number': number,
        }

        total_points = median * 8

        for index, attribute in enumerate(cls.attributes):
            if index > 2:
                offset_down = index * offset_size
                offset_up = (7 - index) * offset_size
            else:
                offset_down = -2 * offset_size
                offset_up = 7 * offset_size

            attr_value = random.randint(median - offset_down, median + offset_up)

            if index == 7:
                attr_value = total_points
                total_points = 0
            else:
                total_points -= attr_value

            attributes[attribute] = attr_value

        return cls(**attributes)

class GoalKeeper(Player):
    attributes = ('jumping',
                  'anticipation',
                  'positioning',
                  'agility',
                  'stamina',
                  'defense',
                  'speed',
                  'offense')

    def __init__(self,
                 name,
                 number,
                 speed,
                 agility,
                 stamina,
                 offense,
                 defense,
                 anticipation,
                 positioning,
                 jumping):
        super(GoalKeeper, self).__init__(name, number, speed, agility, stamina, offense, defense)

        self.anticipation = anticipation
        self.positioning = positioning
        self.jumping = jumping

class Defender(Player):
    attributes = ('marking',
                  'movement',
                  'stealing',
                  'defense',
                  'speed',
                  'stamina',
                  'agility',
                  'offense')

    def __init__(self,
                 name,
                 number,
                 speed,
                 agility,
                 stamina,
                 offense,
                 defense,
                 movement,
                 marking,
                 stealing):
        super(Defender, self).__init__(name, number, speed, agility, stamina, offense, defense)

        self.movement = movement
        self.marking = marking
        self.stealing = stealing

class Wing(Player):
    attributes = ('progression',
                  'crossing',
                  'dribbling',
                  'speed',
                  'stamina',
                  'offense',
                  'defense',
                  'agility')

    def __init__(self,
                 name,
                 number,
                 speed,
                 agility,
                 stamina,
                 offense,
                 defense,
                 progression,
                 crossing,
                 dribbling):
        super(Wing, self).__init__(name, number, speed, agility, stamina, offense, defense)

        self.progression = progression
        self.crossing = crossing
        self.dribbling = dribbling

class Midfielder(Player):
    attributes = ('passing',
                  'arming',
                  'marking',
                  'stamina',
                  'speed',
                  'offense',
                  'defense',
                  'agility')

    def __init__(self,
                 name,
                 number,
                 speed,
                 agility,
                 stamina,
                 offense,
                 defense,
                 marking,
                 passing,
                 arming):

        super(Midfielder, self).__init__(name, number, speed, agility, stamina, offense, defense)

        self.marking = marking
        self.passing = passing
        self.arming = arming

class Striker(Player):
    attributes = ('kicking',
                  'heading',
                  'dribbling',
                  'offense',
                  'agility',
                  'stamina',
                  'speed',
                  'defense')

    def __init__(self,
                 name,
                 number,
                 speed,
                 agility,
                 stamina,
                 offense,
                 defense,
                 kicking,
                 dribbling,
                 heading):
        super(Striker, self).__init__(name, number, speed, agility, stamina, offense, defense)

        self.kicking = kicking
        self.dribbling = dribbling
        self.heading = heading

