# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Top down recursion approach -- requires child subtree heights be redundantly calculated
    # Can be improved by using bottom-up recursion
    # Space O(n)  May check all nodes if tree is skewed
    # Time O(nlogn)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        elif abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def getHeight(self, root) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
