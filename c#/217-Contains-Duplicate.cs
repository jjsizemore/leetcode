// Time		O(n)
// Space	O(n)
public class Solution
{
    public bool hasDuplicate(int[] nums)
    {
        var seen = new HashSet<int>();
        foreach (int i in nums)
        {
            if (seen.Contains(i))
            {
                return true;
            }
            seen.Add(i);
        }
        return false;
    }
}
