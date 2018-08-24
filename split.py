#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/5 下午2:27
# @Author : Sui Chen


def split(ori, seperators=None, protectors=None, keep_seperator=False):
    """
    :type ori: str 被分割的字符串
    :type seperator: str 分隔符, 为空或None则按空格区分
    :type protectors: dict 保护符，无视内部分隔符
    :rtype: list
    """
    if protectors is None:
        protectors = {'[': ']'}
    if seperators is None:
        seperators = [' ']
    pro = None
    ans = list()
    l = 0
    in_pro = False
    left_count = 0
    if keep_seperator:
        move = 0
    else:
        move = 1
    for i in range(len(ori)):
        char = ori[i]
        if not in_pro:
            if char in seperators:
                if ori[l: i]:
                    ans.append(ori[l: i])
                l = i + move
            elif char in protectors:
                left_count = 1
                pro = char
                in_pro = True
        else:
            if char == pro:
                left_count += 1
            elif char == protectors[pro]:
                left_count -= 1
                if left_count == 0:
                    ans.append(ori[l: i+1])
                    l = i + 1
                    in_pro = False
    if ori[l:]:
        ans.append(ori[l:])
    return ans


if __name__ == '__main__':
    print split('   chen   suim    ', keep_seperator=False)