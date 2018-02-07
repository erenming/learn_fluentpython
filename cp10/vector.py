# -*- coding: utf-8 -*-
"""
>>> Vector([3.1, 4.2])
Vector([3.1, 4.2])
>>> Vector((3, 4, 5))
Vector([3, 4, 5])
>>> Vector(range(10))
Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])

切片
>>> v1 = Vector([3, 4, 5])
>>> len(v1)
3 >>> v1[0], v1[-1]
(3.0, 5.0)
>>> v7 = Vector(range(7))
>>> v7[1:4]

"""
from __future__ import absolute_import
import sys, math, reprlib, numbers
from array import array
import functools
import operator

try:
    pass
except ImportError:
    pass


class Vector:
    short_name = 'xyzt'
    typecode = 'd'
    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __iter__(self):
        return iter(self._components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
        bytes(array(self.typecode, self)))

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls[self._components[index]]
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} index must be integers'
            return TypeError(msg.format(cls=cls))

    def __getattr__(self, item):
        cls = type(self)

        if len(item) == 1:
            pos = cls.short_name.find(item)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, item))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.short_name:
                error = 'readonly attribute {attr_name}'
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(attr_name=name, cls_name=cls.__name__)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

