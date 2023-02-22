from typing import List

# region 3 Pointers
# The pointers track the following:
#   Rightmost boundary of zeros (the next index to add a zero at)
#   Current elem under consideration
#   Leftmost boundary of twos (next index to add a two at)
# We increment current when placing 0s and 1s because those are added from the left
# We DO NOT increment current when placing 2s because that would lead to skipping values swapped from the twos ptr spot


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, cur, right = 0, 0, len(nums) - 1

        while cur <= right:
            if nums[cur] == 0:
                nums[cur] = nums[left]
                nums[left] = 0
                cur += 1
                left += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur] = nums[right]
                nums[right] = 2
                right -= 1


# endregion
