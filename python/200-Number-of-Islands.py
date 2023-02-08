from typing import List

# region Recursive DFS

# Space O(n)
# Time O(n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(grid, i, j) -> None:
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if grid[i][j] == "0":
                    return
                else:
                    grid[i][j] = "0"
                    dfs(grid, i - 1, j)
                    dfs(grid, i + 1, j)
                    dfs(grid, i, j - 1)
                    dfs(grid, i, j + 1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(grid, r, c)
        return count


# endregion
from collections import deque

# region Iterative BFS
# Time O(n)
# Space O(n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    q.append([r, c])
                    while q:
                        cur = q.popleft()
                        if (
                            cur[0] >= 0
                            and cur[0] < len(grid)
                            and cur[1] >= 0
                            and cur[1] < len(grid[0])
                        ):
                            if grid[cur[0]][cur[1]] == "1":
                                grid[cur[0]][cur[1]] = "0"
                                q.append([cur[0] - 1, cur[1]])
                                q.append([cur[0] + 1, cur[1]])
                                q.append([cur[0], cur[1] - 1])
                                q.append([cur[0], cur[1] + 1])
        return count


# endregion
