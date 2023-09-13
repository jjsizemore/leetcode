from collections import deque, defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        adjList = defaultdict(set)

        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])

        q = deque()

        while len(adjList.keys()) > 2:
            for vertex in adjList.keys():
                # vertex is a leaf if only one adj vertex
                if len(adjList[vertex]) == 1:
                    q.append(vertex)

            while q:
                cur = q.popleft()
                adj = list(adjList[cur])[0]
                adjList[adj].remove(cur)
                adjList.pop(cur)

        return adjList.keys()
