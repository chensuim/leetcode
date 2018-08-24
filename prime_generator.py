#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/16 下午3:47
# @Author : Sui Chen


def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def prime_generator():
    this = 2
    while True:
        if is_prime(this):
            yield this
        this += 1
