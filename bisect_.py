#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/4 下午3:11
# @Author : Sui Chen


def bisect(array, num, l=0, r=None, key=None):
    if r is None:
        r = len(array)
    while l < r:
        m = (l + r) >> 1
        if key:
            middle = key(array[m])
        else:
            middle = array[m]
        if middle <= num:
            l = m + 1
        else:
            r = m
    return l


def bisect_left(array, num, l=0, r=None, key=None):
    if r is None:
        r = len(array)
    while l < r:
        m = (l + r) >> 1
        if key:
            middle = key(array[m])
        else:
            middle = array[m]
        if middle < num:
            l = m + 1
        else:
            r = m
    return l


def count(grid, num):
    ans = 0
    l = 0
    for i in range(len(grid)):
        for j in range(l, len(grid[i])):
            if grid[i][j] >= num:
                break
        ans += l
    return ans


def num_k(grid, k):
    l = grid[0][0]
    r = grid[-1][-1] + 1
    while l < r:
        m = (l + r) >> 1
        index = count(grid, m) + 1
        if index < k:
            l = m + 1
        else:
            r = m
    return l


