# -*- coding: utf-8 -*-
from utils import new_boolean_matrix
"""
Pros
- 代数的な操作が可能
Cons
- 疎行列の場合メモリ効率が悪い
"""


class AdjacentyMatrix(object):
    def __init__(self, n):
        self.n = n
        self._initialize()

    def _initialize(self):
        self.a = new_boolean_matrix(self.n, self.n)

    def add_edge(self, i, j):
        self.a[i][j] = True

    def remove_edge(self, i, j):
        self.a[i][j] = False

    def has_edge(self, i, j):
        return self.a[i][j]

    def out_edges(self, i):
        out = list()
        for j in range(self.n):
            if self.a[i][j]:
                out.append(j)
        return out
    
    def in_edges(self, i):
        deg = list()
        for j in range(self.n):
            if self.a[j][i]:
                deg.append(j)
        return deg
