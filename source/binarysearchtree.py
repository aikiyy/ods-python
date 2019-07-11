# -*- coding: utf-8 -*-
from binarytree import BinaryTree
from base import BaseSet
"""
Problem
- 木の形状がアンバランス
"""


class BinarySearchTree(BinaryTree, BaseSet):
    class Node(BinaryTree.Node):
        def __init__(self, x):
            super(BinaryTree.Node, self).__init__()
            self.x = x

    def __init__(self, iterable=[], nil=None):
        super(BinarySearchTree, self).__init__()
        self.n = 0
        self.nil = nil
        self.add_all(iterable)

    def find_eq(self, x):
        w = self.r
        while w != self.nil:
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        return None

    def find(self, x):
        w = self.r
        z = self.nil
        while w != self.nil:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        if z == self.nil: return None
        return z.x

    def _find_last(self, x):
        w = self.r
        prev = self.nil
        while w != self.nil:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev

    def _new_node(self, x):
        u = BinarySearchTree.Node(x)
        u.left = self.nil
        u.right = self.nil
        u.parent = self.nil
        return u

    def _add_child(self, p, u):
        if p == self.nil:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True

    def add(self, x):
        p = self._find_last(x)
        return self._add_child(p, self._new_node(x))

    def splice(self, u):
        if u.left != self.nil:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = self.nil
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s != self.nil:
            s.parent = p
        self.n -= 1

    def _remove_node(self, u):
        if u.left == self.nil or u.right == self.nil:
            self.splice(u)
        else:
            w = u.right
            while w.left != self.nil:
                w = w.left
            u.x = w.x
            self.splice(w)

    def remove(self, x):
        u = self._find_last(x)
        if u != self.nil and x == u.x:
            self._remove_node(u)
            return True
        return False

    def isBalanced(self, u):
        left_size = self._size(u.left)
        right_size = self._size(u.right)
        if abs(left_size - right_size) <= 1:
            return True
        return False

    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)

    def rotate_left(self, u):
        w = u.right
        w.parent = u.parent
        if w.parent != self.nil:
            if w.parent.left == u:
                w.parent.left = w
            else:
                w.parent.right = w
        u.right = w.left
        if u.right != self.nil:
            u.right.parent = u
        u.parent = w
        w.left = u
        if u == self.r:
            self.r = w
            self.r.parent = self.nil

    def rotate_right(self, u):
        w = u.left
        w.parent = u.parent
        if w.parent != self.nil:
            if w.parent.left == u:
                w.parent.left = w
            else:
                w.parent.right = w
        u.left = w.right
        if u.left != self.nil:
            u.left.parent = u
        u.parent = w
        w.right = u
        if u == self.r:
            self.r = w
            self.r.parent = self.nil
