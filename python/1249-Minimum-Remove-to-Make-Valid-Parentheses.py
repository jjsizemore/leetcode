# region Stack and String Builder
# Time O(N)
#   First loop is N, then hidden loop (popping each item from stack to add to set) is at worst N, then final loop is N
# Space O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openerStack = []
        toRemove = set()

        for idx, char in enumerate(s):
            if char not in "()":
                continue
            elif char == "(":
                openerStack.append(idx)
            elif openerStack:
                openerStack.pop()
            else:
                toRemove.add(idx)

        toRemove = toRemove.union(set(openerStack))

        remainingChars = []
        for idx, char in enumerate(s):
            if idx not in toRemove:
                remainingChars.append(char)

        return "".join(remainingChars)


# endregion
