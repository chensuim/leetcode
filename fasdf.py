class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        height = 0
        if poured == 0:
            return 0.0
        this_layer = [float(poured - 1)]
        if poured >= 1:
            has = [1.0]
        else:
            has = [0.0]
        for j in range(query_row):
            height += 1
            next_layer = [0.0] * (len(this_layer) + 1)
            next_has = [0.0] * (len(next_layer))
            for i in range(len(this_layer)):
                next_layer[i] += this_layer[i] / 2
                next_layer[i+1] += this_layer[i] / 2
            to_continue = False
            for i in range(len(next_layer)):
                if next_layer[i] > 1:
                    next_layer[i] -= 1
                    next_has[i] = 1.0
                    to_continue = True
                else:
                    next_has[i] = next_layer[i]
                    next_layer[i] = 0
            this_layer = next_layer
            has = next_has
            if not to_continue:
                break
        if height == query_row:
            return has[query_glass]
        else:
            return 0.0
s = Solution()
print s.champagneTower(0, 1, 0)