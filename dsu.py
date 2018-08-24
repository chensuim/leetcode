#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/20 下午8:00
# @Author : Sui Chen


class DSU(object):
    def __init__(self, n):
        self.par = [None] * n
        self.sz = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        if self.sz[xr] < self.sz[yr]:
            xr, yr = yr, xr
        self.par[yr] = xr
        self.sz[xr] += self.sz[yr]
