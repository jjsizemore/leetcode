# region Min Heap
# Time O(nlogk) -- Inserting into heap of size k takes O(logk) time & we do that n times
# Space O(k)
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        # Push the points into a minheap, where we negate the distance
        # Negating distance means that when we pop, we pop the largest absolute distance
        for x, y in points:
            dist = -(x**2 + y**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]


# endregion


# region Sort
# Time O(nlogn)
# Space O(n)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        return points[:k]


# endregion
