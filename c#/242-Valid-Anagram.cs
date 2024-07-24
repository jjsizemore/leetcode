// Time 	O(n)
// Space	O(n)
public class Solution
{
    public bool IsAnagram(string s, string t)
    {
        if (s.Length != t.Length)
            return false;
        int[] count = new int[26];

        for (int i = 0; i < s.Length; i++)
        {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        return count.All(x => x == 0);
    }
}

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
