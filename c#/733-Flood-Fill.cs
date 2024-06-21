// Time 	O(n)
// Space	O(log(n))
public class Solution
{
    public int[][] FloodFill(int[][] image, int sr, int sc, int color)
    {
        if (image[sr][sc] == color)
            return image;

        dfs(image, sr, sc, color, image[sr][sc]);
        return image;

        void dfs(int[][] image, int sr, int sc, int color, int prev)
        {
            int rLen = image.Length,
                cLen = image[0].Length;

            if (sr < 0 || sr >= rLen || sc < 0 || sc >= cLen)
                return;

            if (image[sr][sc] == prev)
            {
                image[sr][sc] = color;
                dfs(image, sr - 1, sc, color, prev);
                dfs(image, sr + 1, sc, color, prev);
                dfs(image, sr, sc - 1, color, prev);
                dfs(image, sr, sc + 1, color, prev);
            }
        }
    }
}
