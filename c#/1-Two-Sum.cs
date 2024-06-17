// Time  O(n) where n is nums.Length
// Space O(n) if every elem is unique
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var dict = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int num = nums[i];
            if (dict.ContainsKey(target - num)) 
            {
                return [i, dict[target - num]];
            }
            else
            {
                dict[num] = i;
            }
        }

        return null;
    }
}