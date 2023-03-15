# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# region Simple Iterative In Order Traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            k -= 1
            if not k:
                return root.val
            root = root.right


# endregion

# region Smallest Elem Stack
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        def _scan_left(smallest, stack):
            stack.append(smallest)
            while smallest.left:
                smallest = smallest.left
                stack.append(smallest)

        _scan_left(root, stack)

        while k > 1:
            cur = stack.pop()
            k -= 1
            if cur.right:
                _scan_left(cur.right, stack)

        return stack[-1].val


# endregion
