#region Binary Search
// Time O(logn)
// Space O(1)
public class Solution
{
    public int FindMin(int[] nums)
    {
        // Res should start off with leftmost value incase fully sorted
        // If l < r, we're in fully sorted array -- take min of l & res, then break
        // If l < mid, shift window right, otherwise left
        // Every time we shift window, whichever take min of res & lesser value

        int l = 0;
        int r = nums.Length - 1;
        int res = nums[0];

        while (l <= r)
        {
            if (nums[l] <= nums[r])
            {
                res = Math.Min(res, nums[l]);
                break;
            }

            int m = (r - l) / 2 + l;

            if (nums[m] >= nums[l])
            {
                res = Math.Min(res, nums[l]);
                l = m + 1;
            }
            else
            {
                res = Math.Min(res, nums[m]);
                r = m - 1;
            }
        }
        return res;
    }
}
#endregion Binary Search
