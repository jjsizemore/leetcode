from collections import deque
from typing import List


# region BFS
# Space O(r*c)
# Time O(r*c)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshOranges = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append(
                        (
                            r,
                            c,
                        )
                    )
                elif grid[r][c] == 1:
                    freshOranges += 1
        if not freshOranges:
            return 0
        minutes = 0

        # we should only work through the q and iterate the time if there are more oranges to rot
        while q and freshOranges > 0:
            # iterate through all newly rotten oranges
            # each q cycle is 1 minute
            for _i in range(len(q)):
                x, y = q.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x + dx, y + dy
                    if (
                        0 <= xx < len(grid)
                        and 0 <= yy < len(grid[0])
                        and grid[xx][yy] == 1
                    ):
                        freshOranges -= 1
                        grid[xx][yy] = 2
                        q.append((xx, yy))

            minutes += 1
        return minutes if not freshOranges else -1


# endregion BFS
