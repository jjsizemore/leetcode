from collections import defaultdict


# region Dict and Reverse Linear Search
class TimeMap:
    def __init__(self):
        self.timeMap = defaultdict(lambda: {})

    # Time O(1)
    # Space O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key][timestamp] = value

    # Time O(N) where N is the number of timestamped values for key
    # Space O(N) where N is the number of timestamped values for key, for the reversed copy of timestamp keys
    def get(self, key: str, timestamp: int) -> str:
        for time in reversed(self.timeMap[key]):
            if self.timeMap[key][time] and time <= timestamp:
                return self.timeMap[key][time]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# endregion
