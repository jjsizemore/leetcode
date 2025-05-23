#region Two Pointers
// Time O(n)
// Space O(1)
public class Solution
{
    public bool IsPalindrome(string s)
    {
        int l = 0,
            r = s.Length - 1;

        while (l < r)
        {
            if (!char.IsLetterOrDigit(s[l]))
            {
                l++;
            }
            else if (!char.IsLetterOrDigit(s[r]))
            {
                r--;
            }
            else
            {
                if (char.ToLower(s[l]) != char.ToLower(s[r]))
                {
                    return false;
                }
                l++;
                r--;
            }
        }
        return true;
    }
}

#endregion

#region Build String
// Time		O(n)
// Space	O(n)
public class Solution
{
    public bool IsPalindrome(string s)
    {
        // Convert string to lowercase and build new alphanumeric string
        s = s.ToLower();
        StringBuilder sb = new();
        foreach (char c in s)
        {
            if ((c >= '0' && c <= '9') || (c >= 'a' && c <= 'z'))
            {
                sb.Append(c);
            }
        }
        s = sb.ToString();

        // Iterate through string from left and right and check that values are equal on either side
        int l = 0,
            r = s.Length - 1;
        while (l <= r)
        {
            if (s[l] != s[r])
            {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}
#endregion
