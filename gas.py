#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/1/28 上午10:52
# @Author : Sui Chen
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        gaps = list()
        for i in range(1, len(stations)):
            gaps.append(stations[i] - stations[i - 1])

        def cut(target, gaps):
            count = 0
            for gap in gaps:
                count += int(gap / target)
                if gap % target > 0:
                    count += 1
                count -= 1
            return count

        l = min(gaps) / float(K)
        r = float(max(gaps))
        while l <= r:
            m = (l + r) / 2
            count = cut(m, gaps)
            if count > K:
                l = m + 10 ** (-6)
            else:
                r = m - 10 ** (-6)
        return l


a = Solution()
print a.minmaxGasDist([1,2,3,4,5,6,7,8,9,10], 9)

