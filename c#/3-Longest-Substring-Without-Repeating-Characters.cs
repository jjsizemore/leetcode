public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        int l = 0,
            maxLen = 0;
        HashSet<char> seen = new();

        for (int r = 0; r < s.Length; r++)
        {
            while (seen.Contains(s[r]))
            {
                seen.Remove(s[l]);
                l++;
            }
            seen.Add(s[r]);
            maxLen = Math.Max(maxLen, r - l + 1);
        }
        return maxLen;
    }
}
