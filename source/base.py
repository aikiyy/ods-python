# -*- coding: utf-8 -*-


class BaseCollection(object):
    def __init__(self):
        super(BaseCollection, self).__init__()

    def size(self):
        return self.n

    def __len__(self):
        return self.size()

    def __str__(self):
        return "[" + ",".join([str(x) for x in self]) + "]"

    def __repr__(self):
        return self.__class__.__name__ \
            + "([" + ",".join([repr(x) for x in self]) + "])"


class BaseList(BaseCollection):
    def __init__(self):
        super(BaseList, self).__init__()

    def append(self, x):
        self.add(self.size(), x)

    def add_all(self, iterable):
        for x in iterable:
            self.append(x)

    def add_first(self, x):
        return self.add(0, x)

    def add_last(self, x):
        return self.add(self.size(), x)

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self.size() - 1)

    def __iter__(self):
        for i in range(len(self)):
            yield(self.get(i))
