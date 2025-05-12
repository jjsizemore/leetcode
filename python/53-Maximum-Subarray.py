from typing import List

# region Kadane's Algo / DP
# Space O(1)
# Time O(n)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSubArray = maxSubArray = nums[0]

        for num in nums[1:]:
            # If just the current number is bigger than the subArray up until that point,
            # trash the subArray and start a new one at the current number
            curSubArray = max(num, curSubArray + num)
            maxSubArray = max(maxSubArray, curSubArray)

        return maxSubArray


# endregion
