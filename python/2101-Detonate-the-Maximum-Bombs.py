from collections import defaultdict
from typing import List


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

        def detonate(idx: int, exploded: set) -> None:
            if idx not in exploded:
                exploded.add(idx)
                for newBoom in inRange[idx]:
                    detonate(newBoom, exploded)

        maxDet = 0

        for i in range(len(bombs)):
            exploded = set()
            detonate(i, exploded)
            maxDet = max(maxDet, len(exploded))

        return maxDet
