#region DP (Space Optimized)
// Time: O(n)
// Space: O(1)
// where n is the length of nums

public class Solution {
    public int RobLinear(int[] nums, int start, int end) {
        int prevRob = 0;
        int prevSkip = 0;

        for (int i = start; i < end; i++) {
            int curRob = prevSkip + nums[i];

            int curSkip = Math.Max(prevRob, prevSkip);

            prevRob = curRob;
            prevSkip = curSkip;
        }

        return Math.Max(prevRob, prevSkip);
    }

    public int Rob(int[] nums) {
        if (nums.Length == 1) return nums[0];

        // 2 scenarios, take first not last or take last not first

        int takeFirst = RobLinear(nums, 0, nums.Length - 1);
        int takeLast = RobLinear(nums, 1, nums.Length);

        return Math.Max(takeFirst, takeLast);
    }
}
#endregion