#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/23 下午6:46
# @Author : Sui Chen


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector(object):
    def __init__(self, fr, to):
        self.x = to.x - fr.x
        self.y = to.y - fr.y

    def __mul__(self, other):
        return self.x * other.y - self.y * other.x

    def __str__(self):
        return '%s, %s' % (self.x, self.y)


class Segment(object):
    def __init__(self, fr, to):
        self.first = fr
        self.second = to

    def cross(self, other):
        ff = Vector(self.first, other.first)
        fs = Vector(self.first, other.second)
        sf = Vector(self.second, other.first)
        ss = Vector(self.second, other.second)
        return (ff * fs) * (sf * ss) <= 0


def check_cross(segment, other):
    return segment.cross(other) and other.cross(segment)


A = Point(0, 0)
B = Point(1, 0)
C = Point(0, 1)
D = Point(1, 1)
print check_cross(Segment(A,D), Segment(C,B))