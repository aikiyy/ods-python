# -*- coding: utf-8 -*-
from base import BaseList


class DLList(BaseList):
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def get_node(self, i):
        if i < self.n / 2:
            p = self.dummy.next
            for _ in range(i):
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n, i, -1):
                p = p.prev
        return p

    def get(self, i):
        if i < 0 or i > self.n - 1: raise IndexError()
        return self.get_node(i).x

    def set(self, i, x):
        if i < 0 or i > self.n - 1: raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def _remove(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    def remove(self, i):
        if i < 0 or i > self.n - 1: raise IndexError()
        self._remove(self.get_node(i))

    def add_before(self, w, x):
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i, x):
        if i < 0 or i > self.n: raise IndexError()
        self.add_before(self.get_node(i), x)

    def __iter__(self):
        u = self.dummy.next
        while u != self.dummy:
            yield u.x
            u = u.next

    def checkSize(self):
        u = self.dummy.next
        n = 0
        while u is not self.dummy:
            u = u.next
            n += 1
        if n != self.n:
            raise Exception

    def isPalindrome(self):
        u = self.dummy.next
        p = self.dummy.prev
        while u is not self.dummy and p is not self.dummy:
            if u.x != p.x:
                return False
            u = u.next
            p = p.prev
        return True

    def rotate(self, r):
        self.dummy.next.prev = self.dummy.prev
        self.dummy.prev.next = self.dummy.next

        target_node = self.get_node(r % self.n)
        self.dummy.next = target_node
        self.dummy.prev = target_node.prev
        target_node.prev.next = self.dummy
        target_node.prev = self.dummy

    def truncate(self, i):
        if i < 0 or i > self.n: raise IndexError()
        self.get_node(i).prev.next = self.dummy