from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# region DFS
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        colMap = defaultdict(list)
        leftMax, rightMax = 0, 0
        if not root:
            return []

        def helper(node, col, row):
            if not node:
                return
            else:
                nonlocal leftMax, rightMax
                leftMax = min(leftMax, col)
                rightMax = max(rightMax, col)
                colMap[col].append((row, node.val))
                helper(node.left, col - 1, row + 1)
                helper(node.right, col + 1, row + 1)

        helper(root, 0, 0)

        retVal = []

        for col in range(leftMax, rightMax + 1):
            colMap[col].sort(key=lambda x: x[0])
            retVal.append([val for row, val in colMap[col]])

        return retVal


# endregion
