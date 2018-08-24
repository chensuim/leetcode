#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/26 下午3:13
# @Author : Sui Chen


class BinaryIndexedTree(object):
    def __init__(self, length):
        length += 1
        self.data = [0] * length

    def insert(self, index, num=1):
        index += 1
        while index < len(self.data):
            self.data[index] += num
            index += index & -index

    def get(self, index):
        ans = 0
        while index > 0:
            ans += self.data[index]
            index -= index & -index
        return ans


if __name__ == '__main__':
    bit = BinaryIndexedTree(20)
    for i in range(20):
        bit.insert(i,i)
    for i in range(21):
        print bit.get(i), i

