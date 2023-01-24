class Solution:
    # Dynamic Programming Soln
    # Space O(n)
    # Time O(n)
    def climbStairs(self, n: int) -> int:
        ways = [1 for i in range(n + 1)]
        ways[1] = 2

        for x in range(2, n + 1):
            ways[x] = ways[x - 1] + ways[x - 2]
        return ways[n - 1]
