# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys

try:
    pass
except ImportError:
    pass


def clip(text, max_len: 'int > 0') -> str:
    """
    在max_len前面或后面的第一个空格出截断文本
    :param text:
    :param max_len:
    :return:
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before > 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
        if end is None:
            end = len(text)
        return text[:end].rstrip()


if __name__ == '__main__':
    print(clip('asdf asdf', 5))