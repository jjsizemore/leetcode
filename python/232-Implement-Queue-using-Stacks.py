#region EfficientPushAmortizedPop
class MyQueue:

    def __init__(self):
        self.main = list()
        self.holding = list()
        self.front = int

    # Time O(1)
    # Space O(n) Need space for each elem
    def push(self, x: int) -> None:
        if not self.main:
            self.front = x
        self.main.append(x)


    # Time O(1) Amortized
    # Space O(1)
    def pop(self) -> int:
        # Moving elements to the holding stack reverses the order s.t. the top holding stack elem
        # will be the first "queue" elem. Only should move elems to holding stack once empty
        # to maintain order
        if not self.holding:
            while self.main:
                self.holding.append(self.main.pop())
        return self.holding.pop()

    # Time O(1)
    # Space O(1)
    def peek(self) -> int:
        if self.holding:
            return self.holding[len(self.holding) - 1]
        return self.front

    # Time O(1)
    # Space O(1)
    def empty(self) -> bool:
        return not self.main and not self.holding


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#endregion


#region LessEfficientPush
class MyQueue:

    def __init__(self):
        self.main = list()
        self.holding = list()

    # Time O(n) Each elem is pushed and popped twice except for new one
    # Space O(n) Need space for each elem
    def push(self, x: int) -> None:
        while self.main:
            self.holding.append(self.main.pop())
        self.main.append(x)
        while self.holding:
            self.main.append(self.holding.pop())

    # Time O(1)
    # Space O(1)
    def pop(self) -> int:
        return self.main.pop()

    # Time O(1)
    # Space O(1)
    def peek(self) -> int:
        if self.main:
            return self.main[len(self.main) - 1]

    # Time O(1)
    # Space O(1)
    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#endregion
