from typing import List

# region Array, Space Optimized


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        highest = 0

        for i in range(len(temperatures) - 1, -1, -1):
            if temperatures[i] >= highest:
                highest = temperatures[i]
            else:
                jumps = 1
                while temperatures[i + jumps] <= temperatures[i]:
                    jumps += answer[i + jumps]
                answer[i] = jumps
        return answer


# endregion
