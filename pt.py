#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/3/3 上午10:45
# @Author : Sui Chen

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from time import sleep, time

def party_later(kind='', n=''):
    b = 1
    for i in xrange(10 ** 7):
        b += i
    return kind + n + ' party time!: ' + __name__

def main():
    with ProcessPoolExecutor() as proc_executor:
        with ThreadPoolExecutor(2) as thread_executor:
            start_time = time()
            proc_future1 = proc_executor.submit(party_later, kind='proc', n='1')
            proc_future2 = proc_executor.submit(party_later, kind='proc', n='2')
            proc_future3 = proc_executor.submit(party_later, kind='proc', n='3')
            proc_future4 = proc_executor.submit(party_later, kind='proc', n='4')
            thread_future1 = thread_executor.submit(party_later, kind='thread', n='1')
            for f in as_completed([
              proc_future1, proc_future2, thread_future1, proc_future3, proc_future4]):
                print(f.result())
            end_time = time()
    print('total time to execute four 3-sec functions:', end_time - start_time)

if __name__ == '__main__':
    main()
