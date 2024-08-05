#region Two Pointers
// Time O(n)
// Space O(1)
public class Solution
{
    public int[] TwoSum(int[] numbers, int target)
    {
        int l = 0,
            r = numbers.Length - 1;

        while (l < r)
        {
            int curSum = numbers[l] + numbers[r];
            if (curSum == target)
            {
                return new int[] { l + 1, r + 1 };
            }
            else if (curSum > target)
            {
                r--;
            }
            else
            {
                l++;
            }
        }
        return new int[2];
    }
}
#endregion
