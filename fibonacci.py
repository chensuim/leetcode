#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/4 下午9:58
# @Author : Sui Chen
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        b = time.time()
        result = func(*args, **kwargs)
        print time.time() - b
        return result
    return wrapper


@timeit
def fibonacci_exponent(n):
    n = int(n)
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_exponent(n-1) + fibonacci_exponent(n-2)


@timeit
def fibonacci_n(n):
    a = 0
    b = 1
    for i in range(n):
        b, a = a+b, b
    return b


print fibonacci_n(50)

