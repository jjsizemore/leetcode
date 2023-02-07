# region Left & Right Product Lists
# Space O(n)
# Time O(n)


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts, rightProducts = [1] * len(nums), [1] * len(nums)

        for idx in range(1, len(nums)):
            leftProducts[idx] = leftProducts[idx - 1] * nums[idx - 1]
        print(leftProducts)
        for idx in range(len(nums) - 2, -1, -1):
            rightProducts[idx] = rightProducts[idx + 1] * nums[idx + 1]
        print(rightProducts)
        retVal = [leftProducts[idx] * rightProducts[idx] for idx in range(len(nums))]

        return retVal


# endregion

# region O(1) Space Approach
# Space O(1) -- Return Value doesn't count toward space.
# Algo for getting left products is exactly the same and we just use a variable to keep track of
# the right products for each index
# Time O(n)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        retVal = [1] * len(nums)

        for idx in range(1, len(nums)):
            retVal[idx] = retVal[idx - 1] * nums[idx - 1]
        rightProduct = 1
        for idx in reversed(range(len(nums))):
            retVal[idx] = retVal[idx] * rightProduct
            rightProduct *= nums[idx]

        return retVal


# endregion
