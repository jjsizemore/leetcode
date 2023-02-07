# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import math
from typing import Optional

# region Recursive Traversal w/ Valid Range
# Time O(n)
# Space O(n)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -math.inf, math.inf)

    def validate(self, root, curMin, curMax) -> bool:
        if not root:
            return True

        if root.val >= curMax or root.val <= curMin:
            return False

        return self.validate(root.left, curMin, root.val) and self.validate(
            root.right, root.val, curMax
        )


# endregion
