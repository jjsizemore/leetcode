#region Optimized Stack
// Time O(n)
// Space O(n)
public class Solution {
    public int LargestRectangleArea(int[] heights) {
        // Can use stack that monotonically increases in height
        // Create pairs of idx & height
        // Iterate through heights, while cur height is less than top of stack,
        // pop top & find area under its height from its idx to cur idx
        // Update cur pair's start idx to startIdx of popped pair
        // Any remaining pairs were extendable to end, so find area for each
        // Each time we find area, get max of curMax and area

        // will contain pairs [idx, height]
        var stack = new Stack<int[]>();
        int n = heights.Length;
        int maxArea = 0;

        for (int i = 0; i < n; i++)
        {
            int curHeight = heights[i];
            int startIdx = i;
            while (stack.Any() && stack.Peek()[1] > curHeight)
            {
                var pair = stack.Pop();
                int area = pair[1] * (i - pair[0]);
                startIdx = pair[0];
                maxArea = Math.Max(area, maxArea);
            }
            stack.Push(new int[]{ startIdx, curHeight });
        }

        while (stack.Any())
        {
            var pair = stack.Pop();
            int area = pair[1] * (n - pair[0]);

            maxArea = Math.Max(area, maxArea);
        }

        return maxArea;
    }
}
#endregion