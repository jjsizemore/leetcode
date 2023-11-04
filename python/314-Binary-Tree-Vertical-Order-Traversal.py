from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# region BFS
# Time O(NlogN) because of the sorting on the keys
# Space O(N)
from collections import defaultdict, deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        colMap = defaultdict(list)
        q = deque()
        q.append((0, root))

        while q:
            col, node = q.popleft()

            if node:
                colMap[col].append(node.val)
                q.append((col - 1, node.left))
                q.append((col + 1, node.right))

        return [colMap[col] for col in sorted(colMap.keys())]


# endregion

# region BFS without Sort
# Time O(N) for the BFS traversal
# Space O(N)
#   O(N) for space taken by queue (max 2 rows at a time, largest row is (N + 1)/2 for leaves in full tree, so O((N + 1)/2 * 2) -> O(N))
#   O(N) for dict
from collections import defaultdict, deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        colMap = defaultdict(list)
        q = deque()
        q.append((0, root))

        leftMax, rightMax = 0, 0
        while q:
            col, node = q.popleft()

            if node:
                colMap[col].append(node.val)
                leftMax = min(leftMax, col)
                rightMax = max(rightMax, col)
                q.append((col - 1, node.left))
                q.append((col + 1, node.right))

        return [colMap[col] for col in range(leftMax, rightMax + 1)]


# endregion


# region DFS
# Time O(W*HlogH) where W is num cols and H is num rows
#   We need to sort the rows of the nodes for each column. The max number of nodes in a row is H/2 since they're distributed in a zig zag, so O(H/2*log(H/2)) we need to do this for W columns, so we have O(W*HlogH)
# Space O(N)
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
