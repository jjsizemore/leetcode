from typing import List


# region 2 Pass Binary Search
# Time O(logn)
# Space O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            if nums[right] < nums[middle]:
                left = middle + 1
            else:
                right = middle
        pivot = left

        print(pivot)

        # determine if target is on left or right of pivot & search for it

        if target > nums[-1]:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, len(nums) - 1
        print(left)

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        print(left)

        return left if nums[left] == target else -1


# endregion
