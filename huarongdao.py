#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/28 上午10:59
# @Author : Sui Chen


class Solution(object):
    target = (1,2,3,4,5,0)

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        visited = set()
        de = board[0] + board[1]
        layer = [de]
        res = 0
        while layer:
            next_layer = list()
            for node in layer:
                if tuple(node) == self.target:
                    return res
                next_step = self.find_next_boards(node)
                for b in next_step:
                    if tuple(b) not in visited:
                        visited.add(tuple(b))
                        next_layer.append(b)
            layer = next_layer
            res += 1
        return -1

    def find_position_zero(self, board):
        for i in range(6):
            if board[i] == 0:
                return i

    def find_next_boards(self, board):
        zero_at = self.find_position_zero(board)
        first = board[:]
        second = board[:]
        third = board[:]
        if zero_at == 0:
            first[0], first[1] = first[1], first[0]
            second[0], second[3] = second[3], second[0]
            return [first, second]
        elif zero_at == 1:
            first[0], first[1] = first[1], first[0]
            second[1], second[2] = second[2], second[1]
            third[1], third[4] = third[4], third[1]
            return [first, second, third]
        elif zero_at == 2:
            first[2], first[1] = first[1], first[2]
            second[2], second[5] = second[5], second[2]
            return [first, second]
        elif zero_at == 3:
            first[3], first[0] = first[0], first[3]
            second[3], second[4] = second[4], second[3]
            return [first, second]
        elif zero_at == 4:
            first[4], first[1] = first[1], first[4]
            second[4], second[3] = second[3], second[4]
            third[4], third[5] = third[5], third[4]
            return [first, second, third]
        elif zero_at == 5:
            first[5], first[4] = first[4], first[5]
            second[5], second[2] = second[2], second[5]
            return [first, second]


a = Solution()
print a.slidingPuzzle([[3,2,4],[1,5,0]])