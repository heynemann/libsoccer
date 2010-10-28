#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest

from libsoccer.names import random_name

class TestNames(unittest.TestCase):
    def test_can_get_random_name(self):
        name, last_name = random_name()

        assert name
        assert last_name
