# Definition for a binary tree node.
from ast import List
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# region Recursive BFS
# Space O(n)
# Time O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        retVal = []
        self.traverse(root, retVal, 0)
        return retVal

    def traverse(self, root: Optional[TreeNode], retVal: List[List[int]], level: int) -> None:
        if root is None:
            return
        while len(retVal) <= level:
            retVal.append([])
        retVal[level].append(root.val)
        self.traverse(root.left, retVal, level + 1)
        self.traverse(root.right, retVal, level + 1)


# endregion

# region Iterative BFS
# Time O(n)
# Space O(n)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        retVal = []

        if not root:
            return retVal

        q = deque()
        q.append(root)
        level = 0
        while q:
            size = len(q)

            while size > 0:
                if len(retVal) <= level:
                    retVal.append([])

                cur = q.popleft()
                if cur:
                    retVal[level].append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                size -= 1
            level += 1
        return retVal


# endregion
