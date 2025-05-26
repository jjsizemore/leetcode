#region Multi-source BFS
// Time: O(R * C)
// Space: O(R * C)
public class Solution {
    public void islandsAndTreasure(int[][] grid) {
        // Multi-source BFS
        // Step 1: Add all treasures to a queue as an array
        var q = new Queue<int[]>();
        int R = grid.Length, C = grid[0].Length;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (grid[r][c] == 0) {
                    q.Enqueue(new int[]{r, c});
                }
            }
        }

        // Step 2: Run BFS on each elem in queue
        int[][] dirs = {
            new int[] { -1, 0 }, new int[] { 0, -1 },
            new int[] { 1, 0 }, new int[] { 0, 1 }
        };

        while (q.Count > 0) {
            var cur = q.Dequeue();
            int row = cur[0], col = cur[1];

            foreach (var dir in dirs) {
                int r = row + dir[0];
                int c = col + dir[1];

                if (r >= R || r < 0 || c >= C || c < 0 || grid[r][c] != int.MaxValue) {
                    continue;
                }
                grid[r][c] = grid[row][col] + 1;
                q.Enqueue(new int[]{r, c});
            }
        }
    }
}
#endregion