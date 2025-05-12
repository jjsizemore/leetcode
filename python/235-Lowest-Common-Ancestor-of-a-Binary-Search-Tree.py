# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Space O(1)
    # Time O(h)
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while True:
            # If root is bigger than both, LCA is somewhere in left subtree
            if root.val > p.val and root.val > q.val:
                root = root.left
            # If root smaller than both, LCA is somewhere in right subtree
            elif root.val < p.val and root.val < q.val:
                root = root.right
            # If root is somewhere in between both values, root is LCA
            else:
                return root
