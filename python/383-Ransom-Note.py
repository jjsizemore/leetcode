from collections import defaultdict


class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magCount = defaultdict(lambda: 0)

        for char in magazine:
            magCount[char] += 1

        for char in ransomNote:
            magCount[char] -= 1
            if magCount[char] < 0:
                return False
        return True
