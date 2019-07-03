# -*- coding: utf-8 -*-
from base import BaseList


class SLList(BaseList):
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.n = 0
        self.head = None
        self.tail = None

    def new_node(self, x):
        return SLList.Node(x)

    def push(self, x):
        u = self.new_node(x)
        u.next = self.head
        self.head = u
        if self.n == 0:
            self.tail = u
        self.n += 1
        return x

    def pop(self):
        if self.n == 0: return None
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
            self.tail = None
        return x

    def get_node(self, i):
        u = self.head
        for _ in range(i):
            u = u.next
        return u

    def get(self, i):
        if i < 0 or i > self.n - 1: raise IndexError()
        return self.get_node(i).x

    def remove(self, i):
        if i < 0 or i > self.n - 1: raise IndexError()
        if i == 0: return self.pop()
        u = self.head
        for _ in range(i - 1):
            u = u.next
        w = u.next
        u.next = u.next.next
        self.n -= 1
        return w.x

    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        if i == 0: self.push(x); return True
        u = self.head
        for _ in range(i - 1):
            u = u.next
        w = self.new_node(x)
        w.next = u.next
        u.next = w
        if self.n == i:
            self.tail = w
        self.n += 1
        return True

    def secondLast(self):
        u = self.head
        for _ in range(self.n - 2):
            u = u.next
        return u.x

    def set(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        u = self.head
        for _ in range(i):
            u = u.next
        y = u.x
        u.x = x
        return y
