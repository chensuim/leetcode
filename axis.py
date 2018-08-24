#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/5 下午12:44
# @Author : Sui Chen
import bisect_


class Axis(object):
    def __init__(self):
        self.axis = [0, 10**9]
        self.other = [0, 0]

    def insert(self, a):
        index = bisect_.bisect_left(self.axis, a)
        if self.axis[index] != a:
            self.axis.insert(index, a)
            self.other.insert(index, self.other[index-1])
        return index

    def find(self, a, b):
        a = bisect_.bisect(self.axis, a) - 1
        b = bisect_.bisect_left(self.axis, b)
        if b > a:
            return max(self.other[a: b])
        else:
            return 0


