class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # Iterate around edge, running a dfs on any land seen and turning it into water
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 1:
                return

            grid[r][c] = 1

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n - 1] == 0:
                dfs(i, n - 1)

        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m - 1][j] == 0:
                dfs(m - 1, j)

        # With this new grid, we can iterate through all cells and any time we come across land, count += 1 and run dfs on the island to make it water

        count = 0

        for k in range(m):
            for l in range(n):
                if grid[k][l] == 0:
                    count += 1
                    dfs(k, l)
        return count
