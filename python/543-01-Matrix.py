# region BFS On Zero Cells First
# Space O(r*c)
# Time O(r*c)
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                print([r, c])
                if mat[r][c] == 0:
                    q.append([r, c])
                else:
                    mat[r][c] = -1

        while q:
            x, y = q.popleft()

            for neighbor in [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]:
                curRow, curCol = neighbor[0], neighbor[1]
                if curRow < 0 or curRow >= len(mat) or curCol < 0 or curCol >= len(mat[0]) or mat[curRow][curCol] != -1:
                    continue
                mat[curRow][curCol] = mat[x][y] + 1
                q.append([curRow, curCol])
        return mat

# endregion


# region DP
# Time O(r*c)
# Space O(1)


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else sys.maxsize
                    left = mat[r][c-1] if c > 0 else sys.maxsize
                    mat[r][c] = min(top, left) + 1

        for r in range(len(mat) - 1, -1, -1):
            for c in range(len(mat[0]) - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r+1][c] if r < len(mat) - 1 else sys.maxsize
                    right = mat[r][c+1] if c < len(mat[0]) - 1 else sys.maxsize
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat
# endregion
