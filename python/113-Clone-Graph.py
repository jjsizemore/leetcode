class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


# region DFS


class Solution:
    def __init__(self):
        self.seen = {}

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node

        if node in self.seen:
            return self.seen[node]

        self.seen[node] = Node(node.val)

        for n in node.neighbors:
            self.seen[node].neighbors.append(self.cloneGraph(n))

        return self.seen[node]


# endregion
