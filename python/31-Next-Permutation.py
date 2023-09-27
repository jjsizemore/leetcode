from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1

        # Need to do this to find the first decreasing element from the right
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # If we got all the way to the front, there's no higher permutation. Reverse it and you're done
        if i == 0:
            nums.reverse()
            return

        # Need to swap i - 1 elem with j elem where j elem is the first elem on the right that's bigger than the i - 1 elem
        while nums[j] <= nums[i - 1]:
            j -= 1

        nums[j], nums[i - 1] = nums[i - 1], nums[j]

        # Reverse the numbers from i to end, since these have to be increasing in order to be the smallest poss next permutation
        nums[i:] = nums[len(nums) - 1 : i - 1 : -1]
