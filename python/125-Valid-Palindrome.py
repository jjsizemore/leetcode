class Solution:
  # Space O(n)
  # Time O(n)
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(filter(str.isalnum, s.lower()))
        for idx, char in enumerate(filtered):
            if idx >= len(filtered) / 2:
                return True
            if char != filtered[0-(idx+1)]:
                return False
        return True
