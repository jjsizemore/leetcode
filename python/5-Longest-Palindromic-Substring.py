# region DP Expand Around Center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Indices of the returned substring
        start = end = 0

        def findPalindrome(s: str, left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            oddLen = findPalindrome(s, i, i)
            evenLen = findPalindrome(s, i, i + 1)
            maxLen = max(oddLen, evenLen)

            if maxLen > end - start + 1:
                end = i + maxLen // 2
                start = i - (maxLen - 1) // 2

        return s[start : end + 1]


# endregion
