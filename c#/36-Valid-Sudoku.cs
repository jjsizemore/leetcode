// Time O(n^2) or O(81)
// Space O(n^2) or O(81)
public class Solution
{
    public bool IsValidSudoku(char[][] board)
    {
        Dictionary<int, HashSet<char>> rows = new();
        Dictionary<int, HashSet<char>> cols = new();
        Dictionary<int, HashSet<char>> squares = new();

        for (int r = 0; r < 9; r++)
        {
            for (int c = 0; c < 9; c++)
            {
                char val = board[r][c];
                if (val == '.')
                    continue;

                int squareKey = r / 3 * 3 + c / 3;

                if (
                    rows.TryGetValue(r, out var rowSet) && rowSet.Contains(val)
                    || cols.TryGetValue(c, out var colSet) && colSet.Contains(val)
                    || squares.TryGetValue(squareKey, out var squareSet) && squareSet.Contains(val)
                )
                    return false;

                rows.TryAdd(r, new HashSet<char>());
                cols.TryAdd(c, new HashSet<char>());
                squares.TryAdd(squareKey, new HashSet<char>());

                rows[r].Add(val);
                cols[c].Add(val);
                squares[squareKey].Add(val);
            }
        }
        return true;
    }
}
