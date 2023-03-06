# Definition for a binary tree node.
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
