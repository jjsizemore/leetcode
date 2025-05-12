from typing import List


# region Set Boundaries
# Time O(M*N)
# Space O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        total = len(matrix) * len(matrix[0])
        print(total)

        spiralOrder = []

        while len(spiralOrder) < total:

            for curX in range(left, right + 1):
                spiralOrder.append(matrix[top][curX])

            for curY in range(top + 1, bottom + 1):
                spiralOrder.append(matrix[curY][right])

            if top != bottom:
                for curX in range(right - 1, left - 1, -1):
                    spiralOrder.append(matrix[bottom][curX])
            if left != right:
                for curY in range(bottom - 1, top, -1):
                    spiralOrder.append(matrix[curY][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return spiralOrder


# endregion
