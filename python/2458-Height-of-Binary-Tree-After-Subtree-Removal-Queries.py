# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
import heapq
from typing import List, Optional


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        nodeToLvl = {}
        lvls = collections.defaultdict(list)

        retVal = []

        def dfs(cur, height):
            if not cur:
                return 0
            height += 1
            left = dfs(cur.left, height) + 1
            right = dfs(cur.right, height) + 1
            nodeToLvl[cur.val] = height

            heapq.heappush(
                lvls[height], (-(max(left, right) + height) + 1, height, cur.val)
            )

            return max(left, right)

        dfs(root, -1)

        for q in queries:
            lvl = nodeToLvl[q]

            if len(lvls[lvl]) == 1:
                retVal.append(
                    lvls[lvl - 1][0][1]
                )  # Return height of level above because there's only one node in the deletion level
            elif lvls[lvl][0][2] == q:
                ptr = heapq.heappop(lvls[lvl])
                retVal.append(-lvls[lvl][0][0])
                heapq.heappush(lvls[lvl], ptr)
            else:
                retVal.append(-lvls[lvl][0][0])

        return retVal
