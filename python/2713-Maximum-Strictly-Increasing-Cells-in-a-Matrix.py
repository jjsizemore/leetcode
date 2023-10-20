from collections import defaultdict
from typing import List
from sortedcontainers import SortedSet


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        r = [0] * m  # Will hold largest number of steps so far in that row
        c = [0] * n  # Same but for that column

        myMap = defaultdict(list)
        s = SortedSet()

        # Create map from values to their coords, alongside a list of those values that will be sorted in descending order
        for x in range(m):
            for y in range(n):
                myMap[-mat[x][y]].append((x, y))
                s.add(-mat[x][y])

        # Will hold longest path from that starting value
        temp = [[0] * n for _ in range(m)]

        for val in s:
            for v in myMap[val]:
                curX, curY = v[0], v[1]
                temp[curX][curY] = max(r[curX], c[curY]) + 1

            for v in myMap[val]:
                curX, curY = v[0], v[1]
                r[curX] = max(r[curX], temp[curX][curY])
                c[curY] = max(c[curY], temp[curX][curY])

        return max(max(r), max(c))
