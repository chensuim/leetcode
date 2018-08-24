#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/6/6 上午11:24
# @Author : Sui Chen
from redis import StrictRedis

redis = StrictRedis(host='10.200.3.16', port=6379, db=1, socket_timeout=4, socket_connect_timeout=4)


class Tst(dict):

    def __init__(self):
        self.test = '1234'

    def __repr__(self):
        return set()

a = Tst()
b = {
    1:5,
    2:6
}
redis.set("xxx", b, ex=24)
c = redis.get("xxx")
print eval(c)[1]
d = '{123:123'
print eval(d)

