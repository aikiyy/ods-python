# -*- coding: utf-8 -*-
import random
import numpy as np
from utils import new_array
from base import BaseList


class SkiplistList(BaseList):
    class Node(object):
        def __init__(self, x, h):
            self.x = x
            self.next = new_array(h + 1)
            self.length = np.ones(h + 1, dtype=int)

        def height(self):
            return len(self.next) - 1

    def __init__(self, iterrable = []):
        self._initialize()
        self.add_all(iterrable)

    def _new_node(self, x, h):
        return SkiplistList.Node(x, h)

    def _initialize(self):
        self.h = 0
        self.n = 0
        self.sentinel = self._new_node(None, 32)

    def find_pred(self, i):
        u = self.sentinel
        r = self.h
        j = -1
        while r >= 0:
            while u.next[r] is not None and j + u.length[r] < i:
                j += u.length[r]
                u = u.next[r]
            r -= 1
        return u

    def get(self, i):
        if i < 0 or i > self.n - 1: raise IndexError()
        return self.find_pred(i).next[0].x

    def set(self, i, x):
        if i < 0 or i > self.n - 1: raise IndexError()
        u = self.find_pred(i).next[0]
        y = u.x
        u.x = x
        return y

    def _add(self, i, w):
        u = self.sentinel
        k = w.height()
        r = self.h
        j = -1
        while r >= 0:
            while u.next[r] is not None and j + u.length[r] < i:
                j += u.length[r]
                u = u.next[r]
            u.length[r] += 1
            if r <= k:
                w.next[r] = u.next[r]
                u.next[r] = w
                w.length[r] = u.length[r] - (i - j)
                u.length[r] = i - j
            r -= 1
        self.n += 1
        return u

    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        w = self._new_node(x, self.pick_height())
        if w.height() > self.h:
            self.h = w.height()
        self._add(i, w)

    def remove(self, i):
        if i < 0 or i > self.n: raise IndexError()
        u = self.sentinel
        r = self.h
        j = -1
        while r >= 0:
            while u.next[r] is not None and j + u.length[r] < i:
                j += u.length[r]
                u = u.next[r]
            u.length[r] -= 1
            if j + u.length[r] + 1 == i and u.next[r] is not None:
                x = u.next[r].x
                u.length[r] += u.next[r].length[r]
                u.next[r] = u.next[r].next[r]
                if u == self.sentinel and u.next[r] is None:
                    self.h -= 1
            r -= 1
        self.n -= 1
        return x

    def __iter__(self):
        u = self.sentinel.next[0]
        while u is not None:
            yield u.x
            u = u.next[0]

    def pick_height(self):
        z = random.getrandbits(32)
        k = 0
        while z & 1:
            k += 1
            z = z // 2
        return k