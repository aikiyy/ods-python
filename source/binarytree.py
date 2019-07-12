# -*- coding: utf-8 -*-
from arrayqueue import ArrayQueue


class BinaryTree(object):
    class Node(object):
        def __init__(self):
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        super(BinaryTree, self).__init__()
        self.nil = None
        self.r = None

    def depth(self, u):
        d = 0
        while u != self.r:
            u = u.parent
            d += 1
        return d

    def size(self):
        return self._size(self.r)

    def _size(self, u):
        if u == self.nil: return 0
        return 1 + self._size(u.left) + self._size(u.right)

    def height(self):
        return self._height(self.r)

    def _height(self, u):
        if u == self.nil: return -1
        return 1 + max(self._height(u.left), self._height(u.right))

    # 深さ優先探索
    def traverse2(self):
        u = self.r
        prev = self.nil
        while u != self.nil:
            if prev == u.parent:
                if u.left != self.nil: next = u.left
                elif u.right != self.nil: next = u.right
                else: next = u.parent
            elif prev == u.left:
                if u.right != self.nil: next = u.right
                else: next = u.parent
            else:
                next = u.parent
            prev = u
            u = next

    # 幅優先探索
    def bf_traverse(self):
        q = ArrayQueue()
        if self.r != self.nil: q.add(self.r)
        while q.size() > 0:
            u = q.remove()
            if u.left != self.nil: q.add(u.left)
            if u.right != self.nil: q.add(u.right)

    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w

    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
