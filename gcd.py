#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/4 下午4:17
# @Author : Sui Chen


def gcd(a, b):
    if b == 0 or a == 0:
        return 0
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    print gcd(5, 0)
    print gcd(0, 5)
    print gcd(5, 5)
    print gcd(5, 6)
    print gcd(19000, 453453534542)