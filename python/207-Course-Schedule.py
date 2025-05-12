# region BFS with Kahn's Algorithm for Topological Sorting
from collections import deque

# Space O(V + E)
# Time O(V + E)


class Solution:

    def adjList(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[List[int]]:
        preReqsToCourses = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            preReqsToCourses[prereq].append(course)

        return preReqsToCourses

    def topoBFS(self, numCourses, prerequisites):
        preReqsToCourses = self.adjList(numCourses, prerequisites)

        inDegrees = [0] * numCourses

        # List of numbers of incoming edges for each node
        for course, _prereq in prerequisites:
            inDegrees[course] += 1

        # Queue with all vertices with no incoming edge
        # At least 1 must exist for an acyclic graph
        queue = deque()
        for course in range(numCourses):
            if inDegrees[course] == 0:
                queue.append(course)

        count = 0
        topoOrder = []

        while queue:
            cur = queue.popleft()

            count += 1

            topoOrder.append(cur)

            for desc in preReqsToCourses[cur]:
                inDegrees[desc] -= 1

                if inDegrees[desc] == 0:
                    queue.append(desc)

        if count != numCourses:
            return None
        else:
            return topoOrder

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return True if self.topoBFS(numCourses, prerequisites) else False


# endregion

# region DFS with processing stack -- stack stores all descendants being processed
# Space O(V + E) -- adjacency list dominates space usage
# Time O(V + E)


class Solution:

    def adjList(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[List[int]]:
        preReqsToCourses = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            preReqsToCourses[prereq].append(course)

        return preReqsToCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preReqsToCourses = self.adjList(numCourses, prerequisites)

        visited = set()

        def isCircular(course, stack) -> bool:
            if course in visited:
                if course in stack:
                    return True
                return False

            visited.add(course)
            stack.append(course)

            for desc in preReqsToCourses[course]:
                if isCircular(desc, stack):
                    return True

            stack.pop()
            return False

        for course in range(numCourses):
            if isCircular(course, []):
                return False
        return True


# endregion


# region DFS with array tracking state (3 states: Not Processed, Processing, Fully Processed)
# Time O(V + E)
# Space O(V + E) Required for the adjacency list
class Solution:

    def adjList(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[List[int]]:
        preReqsToCourses = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            preReqsToCourses[prereq].append(course)

        return preReqsToCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preReqsToCourses = self.adjList(numCourses, prerequisites)

        # Vertices each have a state
        # State = 0     : vertex not visted yet. default state
        # State = -1    : currently being processed. either descendants aren't processed or the vertex is still in the call stack
        # State = 1     : vertex & descendants fully processed

        state = [0] * numCourses

        def isCircular(course) -> bool:
            if state[course] == 1:
                return False
            # If the vertex is being processed & the method gets called on it again, there is a cycle
            if state[course] == -1:
                return True

            state[course] = -1

            for desc in preReqsToCourses[course]:
                if isCircular(desc):
                    return True

            state[course] = 1
            return False

        for course in range(numCourses):
            if isCircular(course):
                return False
        return True


# endregion
