// Create a new array of lists, where each array index points to a list of the indices that that char is found at in the string
// Fill the array with empty int lists
// Iterate through each element in the string, adding the index of each element to the list of indices for that char
// For each index list, iterate through all the indices and multiply all the possible start indices (from the last index or -1) by all possible end indices (up to the next index or length of s)
// Add this product to the return value -- this product is the number of substrings that this incidence of this character is unique for
// Return this retVal

// O(N) Space, O(N) Time

public class Solution {
    public int UniqueLetterString(string s) {
        var indices = new List<int>[26];

        for (int i = 0; i < 26; i++)
        {
            indices[i] = new List<int>();
        }

        // Add all indices where each char is seen
        for (int i = 0; i < s.Length; i++)
        {
            indices[s[i] - 'A'].Add(i);
        }

        int retVal = 0;

        foreach (var list in indices)
        {
            for (int i = 0; i < list.Count; i++)
            {
                int prev = i > 0 ? list[i - 1] : -1;
                int next = i < list.Count - 1 ? list[i + 1] : s.Length;

                retVal += (list[i] - prev) * (next - list[i]);
            }
        }

        return retVal;
    }
}
