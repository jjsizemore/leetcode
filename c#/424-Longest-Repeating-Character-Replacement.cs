#region Sliding Window
// Time O(n)
// Space O(1)
public class Solution
{
    public int CharacterReplacement(string s, int k)
    {
        // Sliding window, track l, maxLen, and mostFrequent
        // Iterate through string using r variable
        // Track char counts via array, get new most frequent
        // Subtract most frequent from length to get replacedLen
        // If replacedLen > k, counts[s[l] - 'A']-- and l++
        //	Q: "Why do an if statement instead of a while loop?"
        // 	A: When the condition is true, replacedLen is only 1 greater than k,
        // 		so the condition is only satisfied once. By incrementing l, replacedLen = k
        // 		and the while condition would break.
        //		TL;DR: The while condition is only satisfied once, so you can use an if statement
        // Get maxLen

        int l = 0,
            maxLen = 0,
            mostFrequent = 0;
        int[] counts = new int[26];

        for (int r = 0; r < s.Length; r++)
        {
            counts[s[r] - 'A']++;

            mostFrequent = Math.Max(mostFrequent, counts[s[r] - 'A']);

            int replacedLen = r - l + 1 - mostFrequent;

            if (replacedLen > k)
            {
                counts[s[l] - 'A']--;
                l++;
            }
            maxLen = Math.Max(maxLen, r - l + 1);
        }
        return maxLen;
    }
}
#endregion
