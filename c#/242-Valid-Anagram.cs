// Time 	O(n)
// Space	O(n)
public class Solution
{
    public bool IsAnagram(string s, string t)
    {
        int[] counts = new int[26];

        foreach (char c in s)
        {
            counts[c - 'a']++;
        }

        foreach (char c in t)
        {
            counts[c - 'a']--;
        }

        return Array.TrueForAll(counts, x => x == 0);
    }
}
