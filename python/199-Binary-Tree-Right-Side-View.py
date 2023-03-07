# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# region DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(level, node, rightView):
            if not node:
                return
            if len(rightView) <= level:
                rightView.append(0)
            rightView[level] = node.val

            helper(level + 1, node.left, rightView)
            helper(level + 1, node.right, rightView)

        retVal = []
        helper(0, root, retVal)
        return retVal


# endregion

# region BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()

        if root:
            q.append(root)

        retVal = []
        while q:
            levelSize = len(q)
            for i in range(levelSize):
                cur = q.popleft()

                if i == levelSize - 1:
                    retVal.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return retVal


# endregion
