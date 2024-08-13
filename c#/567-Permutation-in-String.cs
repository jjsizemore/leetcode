#region Counter Array
// Time O(n)
// Space O(1)
public class Solution
{
    public bool CheckInclusion(string s1, string s2)
    {
        if (s1.Length > s2.Length)
            return false;
        // Sliding window, length of s1
        // Slide the window through s2, adding to the count of
        // the char @ right & subtracting from count of char @ left
        // If counts of each char in s1 are same as in window, return true
        // If we get to end, return false
        int[] counts = new int[26];

        for (int i = 0; i < s1.Length; i++)
        {
            counts[s1[i] - 'a']++;
            counts[s2[i] - 'a']--;
        }

        for (int r = s1.Length; r < s2.Length; r++)
        {
            if (counts.Max() == 0)
            {
                return true;
            }
            counts[s2[r - s1.Length] - 'a']++;
            counts[s2[r] - 'a']--;
        }

        return counts.Max() == 0;
    }
}
#endregion
