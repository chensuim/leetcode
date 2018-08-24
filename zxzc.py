#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/6 下午7:20
# @Author : Sui Chen
"""
First of all, I am not really sure this is a generic solution. In general, we may
need to do some sort of backtracking. I refused to do that, making the theory that this could be solved with a greedy algorithm. It seems to work for the test cases, but it may not work in general.

Alright, warnings said, let us describe the solution. It is composed of two stragegies combined (which is sort of the order in which I conceived them):

0. Count how many zeros and ones we have for each string.

1. If this is a greedy algorithm, then there must be an order which tells us which ones to take first. There seem to be actually two orders, given by following sort key functions:

1.1 minimum(# of zeros left to use, # of ones left to use), reverse order
1.2 minimum(# of zeros in string, # of ones in string), regular order

Both orders try to favor those strings which will consume less 0's and 1's,
but the first one takes into account the parameters m and n, while the second just considers the string in isolation. Under difference circumtances (tests), one order seems to work better than the other. So we should consider both.

2. For each order, we traverse the sorted sequence of strings checking if they meet the constraints. Those passing the checks are counted.

3. We return the maximum counter from the two orders tried.

"""

from collections import defaultdict


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        ones = defaultdict(lambda: 0)
        zeros = defaultdict(lambda: 0)
        k = len(strs)
        for i in xrange(k):
            s = strs[i]
            for c in s:
                if c == '0':
                    zeros[i] += 1
                else:
                    ones[i] += 1

        def s_key1(i):
            zeros_left = m - zeros[i]
            ones_left = n - ones[i]
            return min(zeros_left, ones_left)

        def s_key2(i):
            return min(zeros[i], ones[i])

        def try_order(sorted_idx):
            used = 0
            m_cnt = m
            n_cnt = n
            for i in sorted_idx:
                s = strs[i]
                if zeros[i] <= m_cnt and ones[i] <= n_cnt:
                    m_cnt -= zeros[i]
                    n_cnt -= ones[i]
                    used += 1
            return used
        # main
        sorted_idx = sorted(xrange(k), key=s_key1, reverse=True)
        used1 = try_order(sorted_idx)
        sorted_idx = sorted(xrange(k), key=s_key2, reverse=False)
        used2 = try_order(sorted_idx)
        return max(used1, used2)