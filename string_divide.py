#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/29 下午1:10
#  @Author : Sui Chen


def str_divide(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    if set2 - set1:
        return None
    else:
        result_list = []
        for i in range(len(s2)):
            used1 = 0
            coverd2 = 0
            covered = i
            while used1 == 0 or coverd2 == 0:
                for char in s1:
                    if char == s2[covered]:
                        covered += 1
                        if covered == len(s2):
                            coverd2 += 1
                            covered = 0
                used1 += 1
            result_list.append((used1, coverd2, covered))
        return result_list

class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        rest1 = n1
        rest_coverd = 0
        coverd2 = 0
        cover_list = str_divide(s1, s2)
        trap = set()
        for index in range(len(cover_list)):
            if cover_list[index][2] == index:
                trap.add(index)
        if cover_list is None:
            return 0
        while rest1:
            count_result = cover_list[rest_coverd]
            rest1 -= count_result[0]
            coverd2 += count_result[1]
            rest_coverd = count_result[2]
            if rest_coverd in trap:
                number_of_s1_to_use = cover_list[rest_coverd][0]
                number_of_s2_could_cover = cover_list[rest_coverd][1]
                coverd2 += rest1 / number_of_s1_to_use * number_of_s2_could_cover
                rest1 %= number_of_s1_to_use
                break
        return coverd2 / n2

a = Solution()
print a.getMaxRepetitions('acb', 4, 'ab', 2)
