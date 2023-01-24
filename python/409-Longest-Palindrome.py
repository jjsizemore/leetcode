from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)

        for char in s:
            counts[char] += 1

        retVal = 0
        hasOdd = 0

        for count in counts.values():
            if count % 2 == 0:
                retVal += count
            else:
                hasOdd = 1
                retVal += (count - 1)
        return retVal + hasOdd
