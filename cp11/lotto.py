import random

from cp11.tombola import Tombola


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self._balls))