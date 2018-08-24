#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/22 下午3:20
# @Author : Sui Chen
import sys


def get_single():
    return input()


def get_int():
    return int(get_single())


def get_array():
    return sys.stdin.readline().strip().split()


def get_int_array():
    return map(int, get_array())


for i in sys.stdin:
    print i

