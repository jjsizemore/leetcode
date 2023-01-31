# region Sliding Window
# Time O(n)
# Space O(min(n, m)) -- Need space for the HashSet, which is bounded by size of string n and size of charset m
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, start = 0, 0
        charToIdx = {}

        for idx in range(len(s)):
            curChar = s[idx]
            # If the current char has been seen and occurred after start of window,
            # window start needs to be updated to start right after
            # Otherwise,
            if curChar in charToIdx and charToIdx[curChar] >= start:
                start = charToIdx[curChar] + 1
            longest = max(longest, idx - start + 1)
            charToIdx[curChar] = idx

        return longest
# endregion
