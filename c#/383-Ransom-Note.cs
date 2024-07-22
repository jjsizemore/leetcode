public class Solution
{
    public bool CanConstruct(string ransomNote, string magazine)
    {
        int[] counter = new int[26];

        foreach (char c in magazine)
            counter[c - 'a']++;
        foreach (char c in ransomNote)
            if (counter[c - 'a']-- == 0)
                return false;
        return true;
    }
}
