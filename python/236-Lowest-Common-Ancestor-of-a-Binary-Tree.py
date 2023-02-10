# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# region Recursive DFS
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def dfs(curNode):
            if not curNode:
                return False
            left = dfs(curNode.left)
            right = dfs(curNode.right)

            mid = curNode == p or curNode == q

            if mid + left + right >= 2:
                self.retVal = curNode

            return mid or left or right

        dfs(root)

        return self.retVal


# endregion

# region Clever Recursion


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Passes found values up the call stack
        # If cur node is a target it gets passed up
        # If both left and right have passed up values then cur node gets passed up
        # This makes it so that the parent is always passed up whether a target is also a parent
        # Or the LCA is actually a parent of both

        if not root:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left and right) or (root in [p, q]):
            return root
        else:
            return left or right


# endregion
