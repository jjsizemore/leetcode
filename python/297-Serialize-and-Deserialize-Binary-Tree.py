# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


# region Level Order Traversal -- serialize like LeetCode
class Codec:
    # Do level order traversal by keeping track of children in a queue
    # Time O(n)
    # Space O(n)
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        flattened = []

        q = collections.deque([root])

        while q:
            cur = q.popleft()
            if cur:
                flattened.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                flattened.append("")

        return ",".join(flattened)

    # Start converting flattened values to Nodes and adding them to a queue, and then add children to the nodes by iterating through the flattened list while working through the queue
    # Time O(n)
    # Space O(n)
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return

        flattened = data.split(",")

        retVal = TreeNode(flattened[0])

        q = collections.deque([retVal])

        # For each node, its children will be at i and i+1
        # We will iterate i after each child
        idx = 1
        while q:
            cur = q.popleft()
            if idx < len(flattened) and flattened[idx]:
                cur.left = TreeNode(flattened[idx])
                q.append(cur.left)
            idx += 1
            if idx < len(flattened) and flattened[idx]:
                cur.right = TreeNode(flattened[idx])
                q.append(cur.right)
            idx += 1
        return retVal


# endregion

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
