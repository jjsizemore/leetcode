# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# region Iterative BFS
# Time O(V + E)
# Space O(V)


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node

        myMap = {node.val: Node(node.val)}
        q = deque([node])

        while q:
            cur = q.popleft()
            newCur = myMap[cur.val]

            for neighbor in cur.neighbors:
                if neighbor.val not in myMap:
                    myMap[neighbor.val] = Node(neighbor.val)
                    q.append(neighbor)
                newCur.neighbors.append(myMap[neighbor.val])

        return myMap[node.val]


# endregion

# region Iterative DFS
# Time O(V + E)
# Space O(V)


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node

        myMap = {node.val: Node(node.val)}
        stack = [node]

        while stack:
            cur = stack.pop()
            newCur = myMap[cur.val]

            for neighbor in cur.neighbors:
                if neighbor.val not in myMap:
                    myMap[neighbor.val] = Node(neighbor.val)
                    stack.append(neighbor)
                newCur.neighbors.append(myMap[neighbor.val])

        return myMap[node.val]


# endregion

# region Recursive DFS
# Time O(V + E)
# Space O(V)


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        return self.clone(node, {})

    def clone(self, node, myMap) -> Node:
        if not node:
            return node

        if node.val not in myMap:
            myMap[node.val] = Node(node.val)

        for n in node.neighbors:
            if n.val not in myMap:
                myMap[n.val] = self.clone(n, myMap)
            myMap[node.val].neighbors.append(myMap[n.val])
        return myMap[node.val]


# endregion
