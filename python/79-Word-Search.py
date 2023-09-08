class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def dfs(r, c, idx) -> bool:
            if idx == len(word):
                return True

            if not (0 <= r < len(board) and 0 <= c < len(board[0])):
                return False
            if visited[r][c]:
                return False
            if board[r][c] != word[idx]:
                return False

            visited[r][c] = True

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, idx + 1):
                    return True

            visited[r][c] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
