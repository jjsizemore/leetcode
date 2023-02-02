from collections import deque

# region Evaluate w/ Stack
# Time O(n)
# Space O(n)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["+", "-", "*", "/"])

        q = deque()

        for token in tokens:
            if token not in ops:
                q.append(int(token))
            else:
                if token is "+":
                    q.append(q.pop() + q.pop())
                elif token is "-":
                    second = q.pop()
                    first = q.pop()
                    q.append(first - second)
                elif token is "/":
                    second = q.pop()
                    first = q.pop()
                    q.append(int(first / second))
                else:
                    q.append(q.pop() * q.pop())
            print(q[-1])
        return q.pop()

# endregion
