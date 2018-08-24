#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/19 下午7:58
# @Author : Sui Chen
from kth_smallest import pick


def rank_more(nums, indexes, num):
    def A(i, j):
        return nums[indexes[i]][indexes[j]]
    res = 0
    j = 0
    for i in range(len(indexes)):
        while j < len(indexes):
            if A(i, ~j) <= num:
                break
            j += 1
        res += j
    return res


def rank_less(nums, indexes, num):
    def A(i, j):
        return nums[indexes[i]][indexes[j]]
    res = 0
    j = 0
    for i in range(len(indexes)):
        while j < len(indexes):
            if A(~i, j) >= num:
                break
            j += 1
        res += j
    return res


def nums_between(nums, indexes, a, b):
    def A(i, j):
        return nums[indexes[i]][indexes[j]]
    res = list()
    b_indexes = list()
    a_indexes = list()
    j = 0
    for i in range(len(indexes)):
        while j < len(indexes):
            if A(i, ~j) <= b:
                b_indexes.append(len(indexes) - j)
                break
            j += 1
        else:
            b_indexes.append(len(indexes) - j)
    j = 0
    for i in range(len(indexes)):
        while j < len(indexes):
            if A(~i, j) >= a:
                a_indexes.append(j)
                break
            j += 1
        else:
            a_indexes.append(j)
    a_indexes.reverse()
    for i in range(len(indexes)):
        for j in range(b_indexes[i], a_indexes[i]):
            res.append(A(i, j))
    return res


def twoD_bisect(nums, indexes, k1, k2):
    def A(i, j):
        return nums[indexes[i]][indexes[j]]
    if len(indexes) <= 2:
        res = list()
        n = len(indexes)
        for i in range(n):
            for j in range(n):
                res.append(A(i, j))
        res.sort()
        return res[k1-1], res[k2-1]
    new_indexes = list()
    for i, index in enumerate(indexes):
        if i & 1 == 0 or i == len(indexes) - 1:
            new_indexes.append(index)
    n = len(indexes)
    if n & 1:
        k1_ = (k1 + 2 * n + 1 + 3) / 4
    else:
        k1_ = (k1 + 3) / 4 + n + 1
    k2_ = (k2 + 3) / 4
    a, b = twoD_bisect(nums, new_indexes, k1_, k2_)
    rb_more = rank_more(nums, indexes, b)
    ra_less = rank_less(nums, indexes, a)
    res = nums_between(nums, indexes, a, b)
    if ra_less <= k1 - 1:
        k1th = a
    elif rb_more <= n ** 2 - k1:
        k1th = b
    else:
        k1th = pick(res, k1 + rb_more - n ** 2)
    if ra_less <= k2 - 1:
        k2th = a
    elif rb_more <= n ** 2 - k2:
        k2th = b
    else:
        k2th = pick(res, k2 + rb_more - n ** 2)
    return k1th, k2th


def pick_from_array(nums, k):
    # nums: List[List[]](row and column sorted)
    # k: int
    # return: kth smallest in nums, int
    x, y = twoD_bisect(nums, range(len(nums)), k, k)
    return x


a = [5,4,3,2,1][::-1]


class Column(object):
    def __init__(self, num):
        self.num = num

    def __getitem__(self, item):
        return a[item] + self.num

    def __str__(self):
        res = list()
        for i in range(len(a)):
            res.append(self[i])
        return str(res)

b = map(lambda x: Column(x), a)
print pick_from_array(b, 25)
