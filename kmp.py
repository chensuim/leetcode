#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/21 下午4:34
# @Author : Sui Chen


def kmp(s):
    ans = [0] * len(s)
    ans.append(-1)
    for index, char in enumerate(s):
        last = ans[index-1]
        while last >= 0 and s[last] != char:
            last = ans[last-1]
        ans[index] = last + 1
    ans.pop()
    return ans


print kmp('aaa')

