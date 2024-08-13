#region Count Array
// Time O(n)
// Space O(1)
public class Solution
{
    public string MinWindow(string s, string t)
    {
        // Get count of chars in t, create l ptr, shortestLen, and resL/resR,
        //  which will be used to return substring and updated when shortestLen changes
        // Iterate through s, decrementing counts until all are <=0
        // Tracking l ptr, check if removing char at l will make any count > 0
        // If not, remove char and increment l, then check r - l + 1
        //  and if smaller than smallest seen, save pointers
        // If resL == resR, return "" otherwise return s.Substring(resL, shortestLen)

        int[] count = new int[52];
        int l = 0,
            shortestLen = s.Length,
            resL = 0,
            resR = -1;

        foreach (char c in t)
        {
            AlterCount(count, c, true);
        }

        for (int r = 0; r < s.Length; r++)
        {
            AlterCount(count, s[r], false);
            // All chars in t are in this substring
            while (count.Max() <= 0)
            {
                if (shortestLen >= r - l + 1)
                {
                    shortestLen = r - l + 1;
                    resL = l;
                    resR = r;
                }
                AlterCount(count, s[l], true);
                l++;
            }
        }
        return resR == -1 ? "" : s.Substring(resL, shortestLen);
    }

    public void AlterCount(int[] count, char c, bool increment)
    {
        if (increment)
        {
            if (char.IsUpper(c))
            {
                count[c - 'A' + 26]++;
            }
            else
            {
                count[c - 'a']++;
            }
        }
        else
        {
            if (char.IsUpper(c))
            {
                count[c - 'A' + 26]--;
            }
            else
            {
                count[c - 'a']--;
            }
        }
    }
}
#endregion
