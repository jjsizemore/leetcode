import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = collections.defaultdict(lambda: [])

        for word in strs:
            counts = [0] * 26
            for char in list(word):
                counts[ord(char) - ord("a")] += 1

            groupings[tuple(counts)].append(word)

        retVal = []

        for group in groupings.values():
            retVal.append(group)

        return retVal
