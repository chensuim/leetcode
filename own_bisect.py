#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/3 上午10:24
# @Author : Sui Chen


def bisect(array, num, l=0, r=None, key=None):
    if r is None:
        r = len(num)
    if key is None:
        key = lambda x: x
    while l < r:
        m = (l + r) >> 1
        if key(array[m]) <= num:
            l = m + 1
        else:
            r = m
    return l


def bisect_left(array, num, l=0, r=None, key=None):
    if r is None:
        r = len(num)
    if key is None:
        key = lambda x: x
    while l < r:
        m = (l + r) >> 1
        if key(array[m]) < num:
            l = m + 1
        else:
            r = m
    return l