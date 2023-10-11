import collections


class Logger:
    def __init__(self):
        self.msgs = collections.defaultdict(set)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        for ts in range(timestamp, timestamp - 10, -1):
            if message in self.msgs[ts]:
                return False
        self.msgs[timestamp].add(message)
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
