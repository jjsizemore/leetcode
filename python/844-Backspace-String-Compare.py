import itertools


# region Two Pointers Pythonic
# Time O(m + n)
# Space O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def myFunc(u: str):
            skips = 0
            for char in reversed(u):
                if char == "#":
                    skips += 1
                elif skips:
                    skips -= 1
                else:
                    yield char

        return all(x == y for x, y in itertools.zip_longest(myFunc(s), myFunc(t)))


# endregion


# region Two Pointers
# Time O(m + n) where n and m are the lengths of the strings
# Space O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        skipS, skipT = 0, 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True


# endregion


# region String Builder Solution
# Time O(n + m) where n and m are the lengths of the strings
# Space O(n + m)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(input: str) -> str:
            chars = []
            for elem in input:
                if elem != "#":
                    chars.append(elem)
                elif chars:
                    chars.pop()
            return "".join(chars)

        return build(s) == build(t)


# endregion
