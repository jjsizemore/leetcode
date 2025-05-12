from typing import List

# region Collect Left & Right
# Space O(n)
# Time O(n)


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        curStart, curEnd = newInterval[0], newInterval[1]

        left, right = [], []

        for i in intervals:
            if i[1] < curStart:
                left.append(i)
            elif i[0] > curEnd:
                right.append(i)
            else:
                curStart = min(curStart, i[0])
                curEnd = max(curEnd, i[1])
        return left + [[curStart, curEnd]] + right


# endregion

# region  Hacky Linear Search -- Can be improved
# Space O(N)
# Time O(N)


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        retVal = []

        curStart, curEnd = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            interval = intervals[i]
            # Old interval ends before curStart
            if interval[1] < curStart:
                retVal.append(interval)
                continue
            # Cur interval start overlaps with old
            if (
                interval[0] <= curStart
                and curStart <= interval[1]
                or (curEnd >= interval[0] and curEnd <= interval[1])
            ):
                curStart = min(interval[0], curStart)
                curEnd = max(curEnd, interval[1])
            if interval[0] > curEnd:
                retVal.append([curStart, curEnd])
                retVal.extend(intervals[i:])
                return retVal
        retVal.append([curStart, curEnd])
        return retVal


# endregion
