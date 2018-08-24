#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/24 下午9:14
# @Author : Sui Chen


def sorted_sum(a, b, l, h):
    class Row(object):
        def __init__(self, val):
            self.val = val

        def __getitem__(self, item):
            return self.val + b[item]

    matrix = map(lambda x: Row(x), a)
    res = 0
    right = 0
    left = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if matrix[~i][j] <= h:
                right += 1
            if matrix[~i][j] < l:
                left += 1
        res += right - left
    return res
