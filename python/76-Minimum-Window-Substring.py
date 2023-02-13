from collections import Counter
import math

# region Sliding Window
# Time O(|S| + |T|) where |S| and |T| are the lengths of S & T. Worst case, we have to visit every char in S twice
# Space O(|S| + |T|) -- |S| when window is size of S, |T| when all T chars are unique


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tCounts = Counter(t)

        tUnique = len(tCounts)

        # Number of chars that are at desired frequency in the current substring
        formed = 0

        left, right = 0, 0

        # ans tuple (window length, left, right)
        ans = math.inf, 0, 0

        wCounts = {}

        while right < len(s):

            char = s[right]
            wCounts[char] = wCounts.get(char, 0) + 1

            if char in tCounts and wCounts[char] == tCounts[char]:
                formed += 1

            while left <= right and formed == tUnique:
                if right - left + 1 < ans[0]:
                    ans = right - left + 1, left, right

                char = s[left]
                wCounts[char] -= 1
                if char in tCounts and wCounts[char] < tCounts[char]:
                    formed -= 1
                left += 1

            right += 1

        return "" if ans[0] == math.inf else s[ans[1] : ans[2] + 1]


# endregion
