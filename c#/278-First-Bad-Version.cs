/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

// Time: O(log(n))
// Space: O(n)
public class Solution : VersionControl
{
    public int FirstBadVersion(int n)
    {
        int l = 0,
            r = n;
        while (l < r)
        {
            int mid = l + (r - l) / 2;
            if (IsBadVersion(mid))
            {
                r = mid;
            }
            else
            {
                l = mid + 1;
            }
        }
        return l;
    }
}
