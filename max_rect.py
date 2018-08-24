#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/8/17 下午5:01
# @Author : Sui Chen


def get_max_rect(height_list):
    if len(height_list) == 1:
        return height_list[0]
    elif len(height_list) == 0:
        return 0
    min_index = find_min_rect(height_list)
    max_rect = height_list[min_index] * len(height_list)
    return max(get_max_rect(height_list[:min_index]), get_max_rect(height_list[min_index+1:]), max_rect)


def find_min_rect(height_list):
    min_index = 0
    for index, height in enumerate(height_list):
        if height < height_list[min_index]:
            min_index = index
    return min_index


def get_max_rect_On(height_list):
    ret = 0
    height_list.append(0)
    index = list()
    for i, height in enumerate(height_list):
        while index and height_list[index[-1]] >= height:
            h = height_list[index[-1]]
            index.pop()
            sidx = index[-1] if index else -1
            ret = max(ret, h * (i - 1 - sidx))
        index.append(i)

    return ret

class Solution(object):
    @staticmethod
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ret = 0
        num_columns = len(matrix[0])
        height = [0] * num_columns
        for row in matrix:
            for i in xrange(num_columns):
                height[i] = height[i] + 1 if row[i] else 0
            ret = max(get_max_rect_On(height), ret)

        return ret


def maximalConnected(matrix):
    if not matrix or not matrix[0]:
        return 0

    visited = [[0] * len(matrix[0]) for _ in matrix]

    def relax(i, j):
        count = 0
        if not visited[i][j]:
            visited[i][j] = 1
            if matrix[i][j] != 0:
                count += 1
                if i > 0:
                    count += relax(i-1, j)
                if i < len(matrix) - 1:
                    count += relax(i+1, j)
                if j > 0:
                    count += relax(i, j-1)
                if j < len(matrix[i]) - 1:
                    count += relax(i, j+1)
        else:
            pass
        return count

    def find_not_visited_one():
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] and not visited[i][j]:
                    return i, j
        return None, None
    ret = 0
    while True:
        i, j = find_not_visited_one()
        if i is None:
            return ret
        ret = max(ret, relax(i, j))

print maximalConnected([[1, 0, 1], [1,0,1],[1,1,0],[1,1,0]])