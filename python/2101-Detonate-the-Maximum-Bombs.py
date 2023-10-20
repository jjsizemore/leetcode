from collections import defaultdict
from typing import List


# region Recursive DFS
# Time O(n^2) for pre-processing
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        inRange = defaultdict(list)

        for i, bombi in enumerate(bombs):
            for j, bombj in enumerate(bombs):
                if i != j:
                    distance = (
                        (bombi[0] - bombj[0]) ** 2 + (bombi[1] - bombj[1]) ** 2
                    ) ** (1 / 2)
                    if distance <= bombi[2]:
                        inRange[i].append(j)

        def detonate(idx: int, exploded: set) -> int:
            exploded.add(idx)
            for adj in inRange[idx]:
                if adj not in exploded:
                    detonate(adj, exploded)
            return len(exploded)

        maxDet = 0

        for i in range(len(bombs)):
            maxDet = max(maxDet, detonate(i, set()))

        return maxDet


# endregion


# region Iterative DFS
# Time O(n^3)
#   Creating the graph takes n^2, and
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        inRange = defaultdict(list)

        for i, bombi in enumerate(bombs):
            for j, bombj in enumerate(bombs):
                if i != j:
                    distance = (
                        (bombi[0] - bombj[0]) ** 2 + (bombi[1] - bombj[1]) ** 2
                    ) ** (1 / 2)
                    if distance <= bombi[2]:
                        inRange[i].append(j)

        def detonate(idx: int) -> int:
            stack = [idx]
            exploded = set([idx])
            while stack:
                cur = stack.pop()
                for adj in inRange[cur]:
                    if adj not in exploded:
                        exploded.add(adj)
                        stack.append(adj)
            return len(exploded)

        maxDet = 0

        for i in range(len(bombs)):
            maxDet = max(maxDet, detonate(i))

        return maxDet


# endregion
