from typing import List

# region DP & Least Significant Bit


class Solution:
    def countBits(self, n: int) -> List[int]:
        retVal = [0] * (n + 1)

        for i in range(n + 1):
            retVal[i] = retVal[i // 2] + i % 2
        return retVal


# endregion
