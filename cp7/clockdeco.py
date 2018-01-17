# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
import time
import functools
try:
    pass
except ImportError:
    pass

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


# def clock(func):
#     @functools.wraps(func)
#     def clocked(*args):
#         t0 = time.perf_counter()
#         result = func(*args)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         arg_str = ', '.join(repr(arg) for arg in args)
#         print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
#         return result
#     return clocked

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*args):
            t0 = time.perf_counter()
            result = func(*args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_str = ', '.join(repr(arg) for arg in args)
            print(fmt % (elapsed, name, arg_str, result))
            return result
        return clocked
    return decorate