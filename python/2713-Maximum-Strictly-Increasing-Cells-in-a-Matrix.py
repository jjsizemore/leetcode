from collections import defaultdict
from typing import List

from sortedcontainers import SortedSet


# region More Efficient Soln
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])

        vmap = collections.defaultdict(list)

        for i in range(R):
            for j in range(C):
                vmap[mat[i][j]].append((i, j))

        # Max steps that one can go from a given cell
        dp = [[0] * C for _ in range(R)]

        # Max steps in row and col
        row_res, col_res = [0] * R, [0] * C

        # Iterate through the unique values in the matrix, and for each occurrence of the value, check the row_res & col_res arrays,
        for val in sorted(vmap.keys()):
            for i, j in vmap[val]:
                dp[i][j] = max(row_res[i], col_res[j]) + 1
            for i, j in vmap[val]:
                row_res[i] = max(dp[i][j], row_res[i])
                col_res[j] = max(dp[i][j], col_res[j])

        return max(max(row_res), max(col_res))


# endregion


# region Less Efficient Soln
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


# endregion
