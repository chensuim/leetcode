#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/8/7 上午10:30
# @Author : Sui Chen
import time

word = 'a'
exponent = 20
i = 2 ** exponent
with open('output.csv', 'w') as f:
    while i <= 2 ** (exponent+14):
        one_word = word * i
        another_word = word * i
        b = time.time()
        print one_word == another_word
        f.write(str(time.time() - b) + ',')
        i *= 2

