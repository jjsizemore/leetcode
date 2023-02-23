from collections import deque
from typing import List

# region BFS


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """BFS -- visualize the string as a tree where each node represents the substring up until the index at the end of the current word

        n is length of the input string
        Time O(n^3) - for each start index
        """
        q = deque()
        visited = set()

        q.append(0)

        while q:
            start = q.popleft()
            if start in visited:
                continue
            visited.add(start)
            if start == len(s):
                return True
            for word in wordDict:
                if s[start : min(start + len(word), len(s))] == word:
                    q.append(start + len(word))

        return False


# endregion

# region DP


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        DP -- track whether combinations of substrings in s are present in the dict

        Time O(n^3)
        Space O(n)
        """

        covered = [False] * (len(s) + 1)
        covered[0] = True

        words = set(wordDict)

        for curEnd in range(1, len(s) + 1):
            for curStart in range(curEnd):
                if covered[curStart] and s[curStart:curEnd] in words:
                    covered[curEnd] = True
                    # Break here because once curEnd is true we want outer loop to change value
                    break
        return covered[-1]


# endregion
