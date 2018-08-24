#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/17 下午1:40
# @Author : Sui Chen


class Trie(object):
    def __init__(self, words):
        self.data = [None] * 27
        for word in words:
            layer = self.data
            for char in word:
                index = ord(char) - ord('a')
                if layer[index] is None:
                    layer[index] = [None] * 27
                layer = layer[index]
            layer[-1] = True

