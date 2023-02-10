from typing import List

# region Sorting
# Space O(logN) -- sorting the intervals in place takes logN space
# Time O(N*logN) -- sorting takes N*logN time, other than that we do a simple linear scan


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        retVal = []

        for i in intervals:
            if retVal and retVal[-1][1] >= i[0]:
                retVal[-1][1] = max(retVal[-1][1], i[1])
            else:
                retVal.append(i)
        return retVal


# endregion
