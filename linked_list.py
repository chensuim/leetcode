#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/12 下午5:11
# @Author : Sui Chen
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = str()
        head = self
        while head:
            result += str(head.val) + ' -> '
            head = head.next
        return result


def construct_from_list(a_list):
    result = ListNode(0)
    this = result
    for num in a_list:
        new_node = ListNode(num)
        this.next = new_node
        this = this.next
    return result.next
