# region Backtracking
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking Solution
        Space O(N) -- maintaining tempList requires up to N space
        Time O(N * 2^N) -- we copy a list of length at most N at the end of every subset & there are 2^N subsets in total
        """

        def checkSubset(retVal, tempList, nums, start):
            retVal.append(list(tempList))
            for i in range(start, len(nums)):
                tempList.append(nums[i])
                checkSubset(retVal, tempList, nums, i + 1)
                tempList.pop()

        retVal = []

        checkSubset(retVal, [], nums, 0)

        return retVal


# endregion
