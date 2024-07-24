// Time  O(n) where n is nums.Length
// Space O(n) if every elem is unique
public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        Dictionary<int, int> valToIdx = new();

        for (int i = 0; i < nums.Length; i++)
        {
            int comp = target - nums[i];
            if (valToIdx.ContainsKey(comp))
            {
                return new int[] { valToIdx[comp], i };
            }
            valToIdx[nums[i]] = i;
        }
        return null;
    }
}
