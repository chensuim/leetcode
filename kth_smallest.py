#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/19 下午8:18
# @Author : Sui Chen
import random


def partition(nums, lo, hi):
    pivot = random.randint(lo, hi)
    nums[lo], nums[pivot] = nums[pivot], nums[lo]
    pivot = nums[lo]
    l = lo + 1
    r = hi
    while True:
        while l <= hi and nums[l] <= pivot:
            l += 1
        while r > lo and nums[r] > pivot:
            r -= 1
        if r < l:
            break
        nums[l], nums[r] = nums[r], nums[l]
    nums[r], nums[lo] = nums[lo], nums[r]
    return r


# k is normal counting from 1
def pick(nums, k):
    lo = 0
    hi = len(nums) - 1
    k -= 1
    while True:
        j = partition(nums, lo, hi)
        if j < k:
            lo = j + 1
        elif j > k:
            hi = j - 1
        else:
            return nums[j]

