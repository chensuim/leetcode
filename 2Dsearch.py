#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/5 下午1:59
# @Author : Sui Chen


def next_generator(i, j, only_left=False):
    if only_left:
        directions = ((-1, 0), (0, -1))
    else:
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for d in directions:
        ni = i + d[0]
        nj = j + d[1]
        yield ni, nj
