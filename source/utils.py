# -*- coding: utf-8 -*-
import numpy


def new_array(n, dtype=numpy.object):
    return numpy.empty(n, dtype)


def new_boolean_matrix(n, m):
    return numpy.zeros([n, m], numpy.bool_)


def new_boolean_array(n):
    return numpy.zeros(n, numpy.bool_)
