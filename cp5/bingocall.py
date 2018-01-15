# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
import random

try:
    pass
except ImportError:
    pass


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self, *args, **kwargs):
        return self.pick()