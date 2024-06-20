// Time O(log(n))
// Space O(1)
public class Solution
{
    public int Search(int[] nums, int target)
    {
        int l = 0,
            r = nums.Length - 1;

        while (l <= r)
        {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] > target)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return -1;
    }
}
