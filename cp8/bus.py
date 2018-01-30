# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys

try:
    pass
except ImportError:
    pass

class HauntedBus:
    """备受幽灵乘客折磨的校车"""
    def __init__(self, passengers=[]):
        self.passengers = passengers
    def pick(self, name):
        self.passengers.append(name)
    def drop(self, name):
        self.passengers.remove(name)


bus2 = HauntedBus()
bus2.pick('Carrie')

bus3 = HauntedBus()
bus3.pick('Dave')