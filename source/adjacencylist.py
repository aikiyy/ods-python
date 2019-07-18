# -*- coding: utf-8 -*-
from arraystack import ArrayStack
from utils import new_array


class AdjacencyList(object):
    def __init__(self, n):
        self.n = n
        self._initialize()

    def _initialize(self):
        self.adj = new_array(self.n)
        for i in range(self.n):
            self.adj[i] = ArrayStack()

    def add_edge(self, i, j):
        self.adj[i].append(j)

    def remove_edge(self, i, j):
        for k in self.adj[i]:
            if k == j:
                self.adj[i].remove(k)
                return

    def has_edge(self, i, j):
        for k in self.adj[i]:
            if k == j:
                return True
        return False

    def out_edges(self, i):
        return self.adj[i]

    def in_edges(self, i):
        deg = list()
        for j in range(self.n):
            if self.has_edge(j, i):
                deg.append(j)
        return deg
