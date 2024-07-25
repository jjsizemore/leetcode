#region Create Hash Set
// Space O(n)
// Time O(n)
public class Solution
{
    public int LongestConsecutive(int[] nums)
    {
        HashSet<int> numSet = new(nums);
        int res = 0;

        foreach (int num in numSet)
        {
            if (!numSet.Contains(num - 1))
            {
                int length = 1;
                while (numSet.Contains(num + length))
                {
                    length++;
                }
                res = Math.Max(res, length);
            }
        }
        return res;
    }
}

#endregion
