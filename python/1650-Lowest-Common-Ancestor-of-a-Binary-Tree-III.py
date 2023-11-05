# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# region Find Depth
# Time O(H)
# Space O(1)
class Solution:
    def getDepth(self, node):
        depth = 0

        while node:
            node = node.parent
            depth += 1
        return depth

    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        pDepth, qDepth = self.getDepth(p), self.getDepth(q)

        for _ in range(pDepth - qDepth):
            p = p.parent
        for _ in range(qDepth - pDepth):
            q = q.parent

        while p != q:
            p = p.parent
            q = q.parent
        return p


# endregion
