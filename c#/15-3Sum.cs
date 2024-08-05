public class Solution
{
    public List<List<int>> ThreeSum(int[] nums)
    {
        var res = new List<List<int>>();
        Array.Sort(nums);

        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] > 0)
                break;
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int l = i + 1,
                r = nums.Length - 1;
            while (l < r)
            {
                int curSum = nums[i] + nums[l] + nums[r];

                if (curSum > 0)
                {
                    r--;
                }
                else if (curSum < 0)
                {
                    l++;
                }
                else
                {
                    res.Add(new List<int> { nums[i], nums[l], nums[r] });
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1])
                    {
                        l++;
                    }
                }
            }
        }
        return res;
    }
}
