#region Prefix Postfix Solution
// Space O(1)
// Time O(n)
public class Solution
{
    public int[] ProductExceptSelf(int[] nums)
    {
        int prefix = 1,
            postfix = 1;
        int[] rv = new int[nums.Length];

        for (int i = 0; i < nums.Length; i++)
        {
            rv[i] = prefix;
            prefix *= nums[i];
        }

        for (int i = nums.Length - 1; i >= 0; i--)
        {
            rv[i] *= postfix;
            postfix *= nums[i];
        }

        return rv;
    }
}
#endregion
