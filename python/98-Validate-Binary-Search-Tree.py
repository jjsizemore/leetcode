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


# region Iterative Traversal w/ Valid Range
# Space O(n)
# Time O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        stack.append([root, -math.inf, math.inf])

        while stack:
            curNodeAndBounds = stack.pop()
            curNode = curNodeAndBounds[0]
            if curNode.val <= curNodeAndBounds[1] or curNode.val >= curNodeAndBounds[2]:
                return False
            if curNode.left:
                stack.append([curNode.left, curNodeAndBounds[1], curNode.val])
            if curNode.right:
                stack.append([curNode.right, curNode.val, curNodeAndBounds[2]])
        return True


# endregion


# region Recursive In Order Traversal
# Space O(n) -- Worst case when there's a "bad" elem in the rightmost leaf
# Time O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -math.inf

        def inOrder(root) -> bool:
            if not root:
                return True

            if not inOrder(root.left):
                return False

            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inOrder(root.right)

        return inOrder(root)


# endregion
