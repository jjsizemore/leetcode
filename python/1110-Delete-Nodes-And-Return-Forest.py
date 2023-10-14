# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Testing that the coder knows to pass info:
#   downward via arguments
#   upward via return values
# Time: O(N) where N is number of nodes
# Space: O(H + N) where N is height of tree


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete = set(to_delete)
        retVal = []

        def traverse(root, parent_exist):
            if root is None:
                return None

            if root.val in to_delete:
                traverse(root.left, False)
                traverse(root.right, False)
                return None
            else:
                if not parent_exist:
                    retVal.append(root)
                root.left = traverse(root.left, True)
                root.right = traverse(root.right, True)
                return root

        traverse(root, False)

        return retVal
