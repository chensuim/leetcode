#!/bin/python
import collections
import heapq
import math
import os
import random
import re
import sys


def find_host_id(s):
    a,b,c,d = s.strip().split(',')
    return a


def find_score(s):
    a,b,c,d = s.strip().split(',')
    return float(c)


class Buck(object):
    def __init__(self, _id):
        self._id = _id
        self.container = collections.deque()

    def __lt__(self, other):
        return self.container[0][0] > other.container[0][0]

    def __gt__(self, other):
        return self.container[0][0] < other.container[0][0]

    def __eq__(self, other):
        return self.container[0][0] == other.container[0][0]


def paginate(resultsPerPage, results):
    rec = dict()

    for l in results:
        _id = find_host_id(l)
        if _id not in rec:
            rec[_id] = Buck(_id)
        rec[_id].container.append((find_score(l), l))
    heap = list()
    for key in rec:
        heapq.heappush(heap, rec[key])
    ans = list()
    for i in heap:
        print i.container
    while heap:
        ans.append(list())
        popped = list()
        for i in xrange(resultsPerPage):
            if heap:
                last = heapq.heappop(heap)
                ans[-1].append(last.container.popleft()[1])
                if last.container:
                    heapq.heappush(popped, last)
            elif popped:
                last = heapq.heappop(popped)
                ans[-1].append(last.container.popleft()[1])
                if last.container:
                    heapq.heappush(popped, last)
        heap = popped + heap
        heapq.heapify(heap)
    res = list()
    for rec in ans:
        res.extend(rec)
        res.append('')
    res.pop()
    return res


if __name__ == '__main__':
    resultsPerPage = int(raw_input().strip())

    results_count = int(raw_input().strip())

    results = []

    for _ in xrange(results_count):
        results_item = raw_input()
        results.append(results_item)

    res = paginate(resultsPerPage, results)

    print('\n'.join(res))
