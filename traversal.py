#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/21 下午6:22
# @Author : Sui Chen


def inOrder(root):
    stack = list()
    res = list()
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        root = stack.pop()
        res.append(root.val)
        root = root.right


def preOrder(root):
    stack = [root]
    res = list()
    while stack:
        root = stack.pop()
        if root:
            res.append(root.val)
            stack.append(root.right)
            stack.append(root.left)
    return res


def postOrder(root):
    stack = [root]
    res = list()
    while stack:
        root = stack.pop()
        if root:
            res.append(root.val)
            stack.append(root.left)
            stack.append(root.right)
    res.reverse()
    return res
