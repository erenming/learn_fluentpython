# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
import re
import collections

try:
    pass
except ImportError:
    pass


def example1():
    WORD_RE = re.compile(r'\w+')

    index = collections.defaultdict(list)

    with open(sys.argv[1]) as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)

                index[word].append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, k, default=None):
        try:
            return self[k]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, item):
        return str(item) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


def test_str_key_dict():
    """
    Tests for item retrieval using `d[key]` notation::

    >>> d = StrKeyDict([('2', 'two'), ('4', 'four')])
    >>> d['2']
    'two'
    >>> d[4]
    'four'
    >>> d[1]
    Traceback (most recent call last):
        ...
    KeyError: '1'

    Tests for item retrieval using `d.get(key)` notation::
    >>> d.get('2')
    'two'
    >>> d.get(4)
    'four'
    >>> d.get(1, 'N/A')
    'N/A'

    Tests for the `in` operator:

    >>> 2 in d
    True
    >>> 1 in d
    False
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()