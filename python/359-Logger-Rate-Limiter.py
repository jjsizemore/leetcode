import collections

# region Set & Queue


class Logger:
    def __init__(self):
        self.q = collections.deque()
        self.msgs = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q:
            ts, msg = self.q[0]
            if ts > timestamp - 10:
                break
            else:
                self.q.popleft()
                self.msgs.remove(msg)

        if message in self.msgs:
            return False
        else:
            self.q.append((timestamp, message))
            self.msgs.add(message)
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

# endregion Set & Queue

# region HashMap


class Logger:
    def __init__(self):
        self.msgs = collections.defaultdict(set)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        for ts in range(timestamp, timestamp - 10, -1):
            if message in self.msgs[ts]:
                return False
        self.msgs[timestamp].add(message)
        return True


# endregion HashMap

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
