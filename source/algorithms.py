# -*- coding: utf-8 -*-
import random
from utils import new_boolean_array
from sllist import SLList


def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    a0 = merge_sort(a[:m])
    a1 = merge_sort(a[m:])
    merge(a0, a1, a)
    return a


def merge(a0, a1, a):
    i0 = 0
    i1 = 0
    for i in range(len(a)):
        if i0 == len(a0):
            a[i] = a1[i1]
            i1 += 1
        elif i1 == len(a1):
            a[i] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[i] = a0[i0]
            i0 += 1
        else:
            a[i] = a1[i1]
            i1 += 1


def quick_sort(a):
    _quick_sort(a, 0, len(a))


def _quick_sort(a, i, n):
    if n <= 1: return
    x = a[i + random.randrange(n)]
    p, j, q = i - 1, i, i + n
    while j < q:
        print(x, a)
        if a[j] < x:
            p += 1
            a[j], a[p] = a[p], a[j]
            j += 1
        elif a[j] > x:
            q -= 1
            a[j], a[q] = a[q], a[j]
        else:
            j += 1
    _quick_sort(a, i, p-i+1)
    _quick_sort(a, q, n-(q-i))


def bfs(g, r):
    seen = new_boolean_array(g.n)
    q = SLList()
    q.push(r)
    seen[r] = True
    while q.size() > 0:
        i = q.pop()
        for j in g.out_edges(i):
            if seen[j] == False:
                q.push(j)
                seen[j] = True
    print(seen)
