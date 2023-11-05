# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


# region DFS
# Time O(N)
# Space O(N)


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        retVal = 0

        # Helper function takes in NestedInteger and depth
        # Check if NestedInteger is int, if so multiply by depth and add to retVal
        # Else, recursively call helper function on each value in NestedInteger list with incremented depth
        # Iterate through the nested list, calling helper function on each NestedInteger

        def helper(depth: int, nInt: NestedInteger):
            nonlocal retVal
            if nInt.isInteger():
                retVal += depth * nInt.getInteger()
            else:
                for elem in nInt.getList():
                    helper(depth + 1, elem)

        for elem in nestedList:
            helper(1, elem)
        return retVal


# endregion


# region BFS
# Time O(N)
# Space O(N)
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        q = collections.deque(nestedList)

        # Create queue around current nestedList
        # Store length of queue, and iterate through elements in the queue
        # If the element is a nested int, mult by depth and add to retVal, if its a list, add to the end of the queue
        # Once we've iterated through all elements in the original level of the list, increment depth by 1 and repeat the process through the new queue length
        depth = 1
        retVal = 0
        while q:
            count = len(q)
            while count > 0:
                cur = q.popleft()
                if cur.isInteger():
                    retVal += cur.getInteger() * depth
                else:
                    q.extend(cur.getList())
                count -= 1
            depth += 1
        return retVal


# endregion
