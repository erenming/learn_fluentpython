# -*- coding: utf-8 -*-
"""
2d vector implement by python

>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 5)

>>> v = Vector(3, 4)
>>> abs(v)
5.0

>>> v*3
Vector(9, 12)

>>> abs(v*3)
15.0
"""

from __future__ import absolute_import
import sys
from math import hypot
try:
    pass
except ImportError:
    pass


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
