from typing import List

# region DP (Optimized with 1D array)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s & 1:
            return False
        s >>= 1

        dp = [True] + [False] * s

        for num in nums:
            # Iterate down from target and set cur elem as True if it is True or
            # the elem - num is True
            for elem in range(s, num - 1, -1):
                dp[elem] |= dp[elem - num]
        return dp[-1]


# endregion
