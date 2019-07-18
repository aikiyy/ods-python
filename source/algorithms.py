# -*- coding: utf-8 -*-


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
