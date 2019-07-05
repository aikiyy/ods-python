# -*- coding: utf-8 -*-
import random
from utils import new_array
from base import BaseSet


class SkiplistSSet(BaseSet):
    class Node(object):
        def __init__(self, x, h):
            self.x = x
            self.next = new_array(h + 1)

        def height(self):
            return len(self.next) - 1

    def __init__(self, iterrable = []):
        self._initialize()
        self.add_all(iterrable)

    def _new_node(self, x, h):
        return SkiplistSSet.Node(x, h)

    def _initialize(self):
        self.h = 0
        self.n = 0
        self.sentinel = self._new_node(None, 32)
        self.stack = new_array(self.sentinel.height() + 1)

    def find_pred(self, x):
        u = self.sentinel
        r = self.h
        while r >= 0:
            while u.next[r] is not None and u.next[r].x < x:
                u = u.next[r]
            r -= 1
        return u

    def find(self, x):
        u = self.find_pred(x)
        if u.next[0] is None: return None
        return u.next[0].x

    def add(self, x):
        u = self.sentinel
        r = self.h
        while r >= 0:
            while u.next[r] is not None and u.next[r].x < x:
                u = u.next[r]
            if u.next[r] is not None and u.next[r].x == x: return False
            self.stack[r] = u
            r -= 1
        w = self._new_node(x, self.pick_height())
        while self.h < w.height():
            self.h += 1
            self.stack[self.h] = self.sentinel
        for i in range(len(w.next)):
            w.next[i] = self.stack[i].next[i]
            self.stack[i].next[i] = w
        self.n += 1
        return True

    def remove(self, x):
        removed = False
        u = self.sentinel
        r = self.h
        while r >= 0:
            while u.next[r] is not None and u.next[r].x < x:
                u = u.next[r]
            if u.next[r] is not None and u.next[r].x == x:
                removed = True
                u.next[r] = u.next[r].next[r]
                if u == self.sentinel and u.next[r] is None:
                    self.h -= 1
            r -= 1
        if removed: self.n -= 1
        return removed

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