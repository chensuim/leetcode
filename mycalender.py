#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/29 上午11:25
# @Author : Sui Chen
import bisect_


class MyCalendarThree(object):

    def __init__(self):
        self.axis = [0, 10**9]
        self.number = [0, 0]
        self.max_booked = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        start_index = bisect_.bisect_left(self.axis, start)
        if self.axis[start_index] != start:
            self.axis.insert(start_index, start)
            self.number.insert(start_index, self.number[start_index-1])
        end_index = bisect_.bisect_left(self.axis, end)
        if self.axis[end_index] != end:
            self.axis.insert(end_index, end)
            self.number.insert(end_index, self.number[end_index-1])
        for i in range(start_index, end_index):
            self.number[i] += 1
            self.max_booked = max(self.max_booked, self.number[i])
        return self.max_booked

a = MyCalendarThree()
print a.book(1,2)
print a.book(3,4)
print a.book(1.5, 6)
print a.book(0,0.5)
print a.number, a.axis

