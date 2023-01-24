from collections import defaultdict
from typing import List

# region Boyer-Moore -- Best Solution to Grok
# Space O(1)
# Time O(n)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate


# endregion


# region HashMap
# Space O(n)
# Time O(n)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        length = len(nums)
        for num in nums:
            counts[num] += 1
            if counts[num] > length / 2:
                return num
        return 0

# endregion

# region Sorting
# Space O(1) or O(n) if in-place sort disallowed
# Time O(n)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

# endregion
