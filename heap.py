#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/4 下午2:40
# @Author : Sui Chen
import heapq


class MinHeap(object):
    def __init__(self, data=None):
        if data is None:
            data = list()
        self._heap = data
        heapq.heapify(self._heap)

    def append(self, num):
        heapq.heappush(self._heap, num)

    def pop(self):
        return heapq.heappop(self._heap)

    def get(self):
        return self._heap[0]

    def poppush(self, num):
        return heapq.heapreplace(self._heap, num)

    def pushpop(self, num):
        return heapq.heappushpop(self._heap, num)

    def __nonzero__(self):
        return bool(self._heap)


class MaxHeap(object):
    def __init__(self, data=None):
        if data is None:
            data = list()
        self._heap = [-x for x in data]
        heapq.heapify(self._heap)

    def append(self, num):
        heapq.heappush(self._heap, -num)

    def pop(self):
        return -heapq.heappop(self._heap)

    def get(self):
        return -self._heap[0]

    def poppush(self, num):
        return -heapq.heapreplace(self._heap, -num)

    def pushpop(self, num):
        return -heapq.heappushpop(self._heap, -num)

    def __nonzero__(self):
        return bool(self._heap)


if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,9]
    max_heap = MaxHeap(data)
    max_heap.append(5)
    max_heap.append(6)
    print max_heap.pop()
    print max_heap.pop()
    max_heap.append(7)
    print max_heap.get()
    print max_heap.poppush(9)
    print max_heap.pushpop(10)