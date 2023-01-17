class Solution:
  # Time O(n+m)
  # Space O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        return all(s.count(x) == s.count(x) for x in string.ascii_lowercase)

