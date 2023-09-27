# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# region Recursion


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


# endregion Recursion

# region Iteration


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []

        def check(p, q) -> bool:
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return True

        stack.append((p, q))

        while stack:
            p, q = stack.pop()

            if not check(p, q):
                return False
            if p:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
        return True


# endregion Iteration
