#region DP (Space Optimized)
// Time: O(n)
// Space: O(1)
// where n is the length of nums

/// <summary>
/// Solution for House Robber II problem (LeetCode 213)
///
/// Problem: You are a professional robber planning to rob houses along a street.
/// Each house has a certain amount of money stashed. All houses at this place are
/// arranged in a circle. That means the first house is the neighbor of the last one.
///
/// Constraint: Adjacent houses have security systems connected, so you cannot rob
/// two adjacent houses. Also, since houses are in a circle, you cannot rob both
/// the first and last house.
///
/// Approach: This is a variant of House Robber I with the circular constraint.
/// We solve it by considering two scenarios:
/// 1. Rob houses from index 0 to n-2 (include first, exclude last)
/// 2. Rob houses from index 1 to n-1 (exclude first, include last)
/// Then take the maximum of both scenarios.
/// </summary>
public class Solution {
    /// <summary>
    /// Solves the linear House Robber problem for a given range of houses.
    /// This is the core dynamic programming logic used by both scenarios.
    ///
    /// Algorithm explanation:
    /// - prevRob: Maximum money if we rob the current house
    /// - prevSkip: Maximum money if we skip the current house
    ///
    /// For each house, we have two choices:
    /// 1. Rob current house: prevSkip + nums[i] (can't rob previous house)
    /// 2. Skip current house: max(prevRob, prevSkip) (take best of previous states)
    /// </summary>
    /// <param name="nums">Array of money in each house</param>
    /// <param name="start">Starting index (inclusive)</param>
    /// <param name="end">Ending index (exclusive)</param>
    /// <returns>Maximum money that can be robbed in the given range</returns>
    public int RobLinear(int[] nums, int start, int end) {
        // prevRob: max money if we robbed the previous house
        int prevRob = 0;
        // prevSkip: max money if we skipped the previous house
        int prevSkip = 0;

        for (int i = start; i < end; i++) {
            // If we rob current house, we must have skipped the previous house
            int curRob = prevSkip + nums[i];

            // If we skip current house, we take the better of previous two states
            int curSkip = Math.Max(prevRob, prevSkip);

            // Update states for next iteration
            prevRob = curRob;
            prevSkip = curSkip;
        }

        // Return the maximum of robbing or skipping the last house in range
        return Math.Max(prevRob, prevSkip);
    }

    /// <summary>
    /// Main method that handles the circular constraint of House Robber II.
    ///
    /// Key insight: Since houses are in a circle, we cannot rob both first and last house.
    /// So we solve two separate linear problems:
    /// 1. Consider houses 0 to n-2 (can rob first, cannot rob last)
    /// 2. Consider houses 1 to n-1 (cannot rob first, can rob last)
    ///
    /// The answer is the maximum of these two scenarios.
    /// </summary>
    /// <param name="nums">Array representing money in each house</param>
    /// <returns>Maximum money that can be robbed without alerting police</returns>
    public int Rob(int[] nums) {
        // Edge case: only one house, rob it
        if (nums.Length == 1) return nums[0];

        // Scenario 1: Rob houses from 0 to n-2 (include first house, exclude last house)
        // This ensures we don't violate the circular constraint
        int takeFirst = RobLinear(nums, 0, nums.Length - 1);

        // Scenario 2: Rob houses from 1 to n-1 (exclude first house, include last house)
        // This ensures we don't violate the circular constraint
        int takeLast = RobLinear(nums, 1, nums.Length);

        // Return the maximum money from both scenarios
        return Math.Max(takeFirst, takeLast);
    }
}
#endregion