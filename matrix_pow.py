#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/24 上午9:57
# @Author : Sui Chen
import time
import copy


def matrix_multi(matrix, other):
    M = 10 ** 9 + 7
    otherT = zip(*other)
    res = list()
    for row in matrix:
        new_row = list()
        for column in otherT:
            summation = 0
            for i in range(len(row)):
                summation += row[i] * column[i]
            new_row.append(summation % M)
        res.append(new_row)
    return res


def pow(matrix, n):
    if n == 1:
        return copy.deepcopy(matrix)
    if n & 1:
        half = pow(matrix, (n-1)/2)
        return matrix_multi(matrix_multi(half, half), matrix)
    else:
        half = pow(matrix, n / 2)
        return matrix_multi(half, half)


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = 10 ** 9 + 7
        matrix = [[1,0,1,0,1,0], [1,1,1,1,1,1],[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0]]
        end_matrix = pow(matrix, n)
        res = sum(zip(*end_matrix)[0]) % M
        return res

solution = Solution()


