from typing import List

# region Backtracking
# Space O(N^(T/M)) where N is num candidates, T is target value, M is minimum candidate
#   This is the max size of the call stack for a combo
#   Recursive calls can pile up to T/M
#   Keeping a combo of numbers during execution takes up to T/M as well
#
# Time O(N^((T/M) + 1))


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        retVal = []

        def backtrack(combo, remain, idx):
            if remain == 0:
                retVal.append(combo.copy())
                return
            elif remain < 0:
                return
            else:
                for curIdx in range(idx, len(candidates)):
                    combo.append(candidates[curIdx])
                    backtrack(combo, remain - candidates[curIdx], curIdx)
                    combo.pop()

        backtrack([], target, 0)
        return retVal


# endregion
