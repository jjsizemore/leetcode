from typing import List

# region DP (Space Optimized)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxRobbed = 0

        twoUp, oneUp = 0, nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            maxRobbed = max(oneUp, twoUp + nums[i])
            twoUp = oneUp
            oneUp = maxRobbed
        return oneUp


# endregion

# region Dynamic Programming


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxRobbed = [0] * (len(nums) + 1)

        maxRobbed[len(nums)], maxRobbed[len(nums) - 1] = 0, nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            maxRobbed[i] = max(maxRobbed[i + 1], maxRobbed[i + 2] + nums[i])
        return maxRobbed[0]


# endregion

# region Recursion with Memoization


class Solution:
    def __init__(self):
        self.memo = {}
        self.nums = []

    def rob(self, nums: List[int]) -> int:
        self.nums = nums

        return self.robFrom(0)

    def robFrom(self, idx: int) -> int:
        if idx >= len(self.nums):
            return 0

        if idx in self.memo:
            return self.memo[idx]

        ans = max(self.robFrom(idx + 1), self.robFrom(idx + 2) + self.nums[idx])

        self.memo[idx] = ans
        return ans


# endregion
