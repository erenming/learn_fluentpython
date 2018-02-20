import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素"""
        pass

    @abc.abstractmethod
    def pick(self):
        """
        随机删除元素并返回其
        若实例为空，则改方法抛出'LookupError'
        :return:
        """
        pass

    def loaded(self):
        """是否还有一个元素"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组，由当前元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))