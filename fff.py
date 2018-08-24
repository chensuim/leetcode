import collections


class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        ds = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def getgroups():
            groups = []
            visited = set()
            for i in range(m):
                for j in range(n):
                    if grid[i][j] != 1 or (i, j) in visited:
                        continue
                    group = set()
                    q = [(i, j)]
                    while q:
                        (x, y) = q.pop(0)
                        visited.add((x, y))
                        group.add((x, y))
                        for (dx, dy) in ds:
                            xx, yy = x + dx, y + dy
                            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1 and (xx, yy) not in visited:
                                visited.add((xx, yy))
                                q.append((xx, yy))
                    groups.append(group)
            return groups

        def expand(group):
            ret = collections.Counter()
            for (i, j) in group:
                for (dx, dy) in ds:
                    xx, yy = i + dx, j + dy
                    if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 0:
                        ret[(xx, yy)] += 1
            return ret

        groups = getgroups()
        print groups
        nwalls = 0

        # for _ in range(m):
        #     print(grid[_])
        # print()

        while groups:
            if sum(len(g) for g in groups) == m * n:
                return nwalls
            walls = [expand(g) for g in groups]

            maxi = -1
            maxunaff = 0

            for i in range(len(walls)):
                tmp = len(walls[i])
                if tmp > maxunaff:
                    maxi, maxunaff = i, tmp

            print([len(wall) for wall in walls])
            for (x, y) in groups[maxi]:
                grid[x][y] = 2

            # for _ in range(m):
            #     print(grid[_])
            # print("Build wall for group {}/{}".format(maxi, len(groups)))
            nwalls += sum(walls[maxi].values())
            walls = walls[:maxi] + walls[maxi + 1:]
            for wall in walls:
                for (x, y) in wall:
                    grid[x][y] = 1
            # for _ in range(m):
            #     print(grid[_])
            # print(nwalls)
            groups = getgroups()
            print groups

        return nwalls




a = Solution()
print a.containVirus([[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
)
