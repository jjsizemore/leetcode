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

# region Monotonic Stack
# Monotonic Stack - A stack where the elements are always in sorted order
# Monotonic decreasing, like the one below, means the stack will always be sorted in descending order
# We store the indices, but the indices are sorted in descending order in terms of the temperatures they correspond to


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for cur_day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                answer[prev_day] = cur_day - prev_day
            stack.append(cur_day)

        return answer


# endregion
