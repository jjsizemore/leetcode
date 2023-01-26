# region  Hacky Linear Search -- Can be improved
# Space O(N)
# Time O(N)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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
            if interval[0] <= curStart and curStart <= interval[1] or (curEnd >= interval[0] and curEnd <= interval[1]):
                curStart = min(interval[0], curStart)
                curEnd = max(curEnd, interval[1])
            if interval[0] > curEnd:
                retVal.append([curStart, curEnd])
                retVal.extend(intervals[i:])
                return retVal
        retVal.append([curStart, curEnd])
        return retVal
# endregion
