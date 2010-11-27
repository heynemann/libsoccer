#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Module responsible for simulating players.
'''

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

from libsoccer.dice import randint
from libsoccer.names import random_name

class Player(object):
    '''
    Abstract Player class.
    '''
    attributes = ('speed', 'agility', 'stamina', 'offense', 'defense')

    def __init__(self, **kw):
        self.name = kw['name']
        self.number = kw['number']
        self.speed = kw['speed']
        self.agility = kw['agility']
        self.stamina = kw['stamina']
        self.offense = kw['offense']
        self.defense = kw['defense']

    def __str__(self):
        return unicode(self)

    def __unicode__(self):
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
        '''Generates a player for the given class'''
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

            attr_value = randint(median - offset_down,
                                 median + offset_up)

            if index == 7:
                attr_value = total_points
                total_points = 0
            else:
                total_points -= attr_value

            attributes[attribute] = attr_value

        return cls(**attributes)

class GoalKeeper(Player):
    '''
    Model that represents a goal keeper
    '''

    attributes = ('jumping',
                  'anticipation',
                  'positioning',
                  'agility',
                  'stamina',
                  'defense',
                  'speed',
                  'offense')

    def __init__(self, **kw):
        super(GoalKeeper, self).__init__(name=kw['name'],
                                         number=kw['number'],
                                         speed=kw['speed'],
                                         agility=kw['agility'],
                                         stamina=kw['stamina'],
                                         offense=kw['offense'],
                                         defense=kw['defense'])

        self.anticipation = kw['anticipation']
        self.positioning = kw['positioning']
        self.jumping = kw['jumping']

class Defender(Player):
    '''
    Model that represents a goal defender
    '''

    attributes = ('marking',
                  'movement',
                  'stealing',
                  'defense',
                  'speed',
                  'stamina',
                  'agility',
                  'offense')

    def __init__(self, **kw):
        super(Defender, self).__init__(name=kw['name'],
                                       number=kw['number'],
                                       speed=kw['speed'],
                                       agility=kw['agility'],
                                       stamina=kw['stamina'],
                                       offense=kw['offense'],
                                       defense=kw['defense'])

        self.movement = kw['movement']
        self.marking = kw['marking']
        self.stealing = kw['stealing']

class Wing(Player):
    '''
    Model that represents a wing
    '''

    attributes = ('progression',
                  'crossing',
                  'dribbling',
                  'speed',
                  'stamina',
                  'offense',
                  'defense',
                  'agility')

    def __init__(self, **kw):
        super(Wing, self).__init__(name=kw['name'],
                                   number=kw['number'],
                                   speed=kw['speed'],
                                   agility=kw['agility'],
                                   stamina=kw['stamina'],
                                   offense=kw['offense'],
                                   defense=kw['defense'])

        self.progression = kw['progression']
        self.crossing = kw['crossing']
        self.dribbling = kw['dribbling']

class Midfielder(Player):
    '''
    Model that represents a midfielder
    '''

    attributes = ('passing',
                  'arming',
                  'marking',
                  'stamina',
                  'speed',
                  'offense',
                  'defense',
                  'agility')

    def __init__(self, **kw):

        super(Midfielder, self).__init__(name=kw['name'],
                                         number=kw['number'],
                                         speed=kw['speed'],
                                         agility=kw['agility'],
                                         stamina=kw['stamina'],
                                         offense=kw['offense'],
                                         defense=kw['defense'])

        self.marking = kw['marking']
        self.passing = kw['passing']
        self.arming = kw['arming']

class Striker(Player):
    '''
    Model that represents a striker
    '''

    attributes = ('kicking',
                  'heading',
                  'dribbling',
                  'offense',
                  'agility',
                  'stamina',
                  'speed',
                  'defense')

    def __init__(self, **kw):
        super(Striker, self).__init__(name=kw['name'],
                                      number=kw['number'],
                                      speed=kw['speed'],
                                      agility=kw['agility'],
                                      stamina=kw['stamina'],
                                      offense=kw['offense'],
                                      defense=kw['defense'])

        self.kicking = kw['kicking']
        self.dribbling = kw['dribbling']
        self.heading = kw['heading']
