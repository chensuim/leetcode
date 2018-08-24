#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/13 下午3:02
# @Author : Sui Chen
import time
from threading import Thread

import sys
from requests.packages.urllib3.util import selectors


def print_hello():
    while True:
        print 'Hello World'
        time.sleep(3)


def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else n


def process_input(stream):
    text = stream.readline()
    n = int(text.strip())
    print('fib({}) = {}'.format(n, fib(n)))


def read_and_process():
    while True:
        n = int(input())
        print ('fib({}) = {}'.format(n, fib(n)))


def read_and_process_2():
    while True:
        n = int(input())
        print ('222222fib({}) = {}'.format(n, fib(n)))


def main():
    selector = selectors.DefaultSelector()
    selector.register(sys.stdin, selectors.EVENT_READ)
    last_hello = 0
    while True:
        for event, mask in selector.select(3):
            print 'here'
            process_input(event.fileobj)
        if time.time() - last_hello > 3:
            last_hello = time.time()
            print_hello()

if __name__ == '__main__':
    main()
