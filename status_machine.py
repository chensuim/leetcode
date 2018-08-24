#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/12/5 下午1:03
# @Author : Sui Chen


class StatusMachine(object):
    def __init__(self, s):
        self._status = 0
        next_dict = dict()
        for index, char in enumerate(s):

