from typing import List

# region Backtracking


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        retVal = []

        def tryPermute(perm):
            if perm in retVal:
                return
            elif len(perm) == len(nums):
                retVal.append(perm.copy())
            else:
                for num in nums:
                    if num not in perm:
                        perm.append(num)
                        tryPermute(perm)
                        perm.pop()

        tryPermute([])

        return retVal


# endregion
