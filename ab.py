#coding=utf-8
import sys


def deal_with_time(t):
    t = t.split(':')
    return int(t[0]) * 3600 + int(t[1]) * 60 + float(t[2])


class Task(object):
    def __init__(self, x, d, t):
        self.x = int(x) - 1
        self.d = int(d.split('.')[2])
        self.t = deal_with_time(t)


class Line(object):
    def __init__(self, s, t, p, t1, t2):
        self.s = int(s) - 1
        self.t = int(t) - 1
        self.p = int(p)
        self.t1 = deal_with_time(t1)
        self.t2 = deal_with_time(t2)


class Pos(object):
    def __init__(self, cost, time):
        self.cost = cost
        self.time = time



if __name__ == "__main__":
    # 读取第一行的n
    n,m,k = map(int, sys.stdin.readline().strip().split())
    tasks = [[] for _ in range(10)]
    for i in range(n):
        x, d, t = sys.stdin.readline().strip().split()
        t = Task(x, d, t)
        tasks[t.d].append(t)
    for i in tasks:
        i.sort(key=lambda x: x.t)
    lines = [[] for _ in range(k)]
    for i in range(m):
        S, T, p, t1, t2 = sys.stdin.readline().strip().split()
        line = Line(S,T,p,t1,t2)
        lines[line.s].append(line)


    def find_min(s, t, t1, t2, d1, d2):
        pos = [None] * k
        pos[s] = [(0, t1), (0, t1)]
        ans = float('inf')
        for d in range(d1, d2+1):
            new_pos = [None] * k
            for i, p in enumerate(pos):
                if p is not None:
                    for j in p:
                        for line in lines[i]:
                            if line.t1 > j[1]:
                                if (d == d2 and line.t2 < t2) or (d != d2):
                                    cost = j[0] + line.p
                                    if cost > ans:
                                        continue
                                    if line.t2 < mmin_time[1]:
                                        mmin_time = (j[0] + line.p, line.t2)
                                    if cost < mmin_cost[0]:
                                        mmin_cost = (cost, line.t2)
                    ans = list()
                    if mmin_time[0] != float('inf'):
                        ans.append(mmin_time)
                    if mmin_cost[0] != float('inf'):
                        ans.append(mmin_cost)
                    if ans:
                        pos[]
            pos = [None] * k
        if ans != float('inf'):
            return ans
        else:
            return -1






    def f():
        ans = 0
        now_at = 1
        for i, day in tasks:
            last = 0
            for j, t in day:
                target = t.x
                dead_line = t.t
                if i == 1:
                    cost = find_min(now_at, target, last, dead_line)
                else:
                    if j == 0:
                        cost = find_cross_day(now_at, target, last, dead_line)
                    else:
                        cost = find_min(now_at, target, last, dead_line)
                if cost == -1:
                    return -1
                else:
                    ans += cost
                    last = dead_line
                    now_at = target
        return ans
    print f()
