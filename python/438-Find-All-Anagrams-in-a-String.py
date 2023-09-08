from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pLen, sLen, retVal, pCounts = len(p), len(s), [], defaultdict(lambda: 0)

        if pLen > sLen:
            return retVal

        for letter in p:
            pCounts[letter] += 1

        # Check initial window
        for idx in range(pLen - 1):
            pCounts[s[idx]] -= 1

        for idx in range(-1, sLen - pLen + 1):
            print(idx)
            if idx > -1:
                pCounts[s[idx]] += 1
            if idx + pLen < sLen:
                pCounts[s[idx + pLen]] -= 1

            if not any(pCounts.values()):
                retVal.append(idx + 1)

        return retVal
