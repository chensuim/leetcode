#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/24 上午11:05
# @Author : Sui Chen
import collections


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        self.conners = collections.defaultdict(lambda: 0)
        left = float('inf')
        right = float('-inf')
        top = left
        bottom = right
        area = 0
        for rectangle in rectangles:
            l, t, r, b = rectangle
            left = min(l, left)
            right = max(r, right)
            top = min(t, top)
            bottom = max(b, bottom)
            self.updateRect(l, t, r, b)
            area += (r - l) * (b - t)
        outerFour = [(left, top), (right, top), (left, bottom), (right, bottom)]
        for outer in outerFour:
            if outer not in self.conners or self.conners[outer] != 1:
                return False
        for conner in self.conners:
            if self.conners[conner] & 1 and conner not in outerFour:
                return False
        return area == (right - left) * (bottom - top)

    def updateRect(self, l, t, r, b):
        self.conners[(l, t)] += 1
        self.conners[(r, t)] += 1
        self.conners[(r, b)] += 1
        self.conners[(l, b)] += 1


a = Solution()
rectangles = [[0,0,4,1],[7,0,8,2],[6,2,8,3],[5,1,6,3],[4,0,5,1],[6,0,7,2],[4,2,5,3],[2,1,4,3],[0,1,2,2],[0,2,2,3],[4,1,5,2],[5,0,6,1]]
print a.isRectangleCover(rectangles)