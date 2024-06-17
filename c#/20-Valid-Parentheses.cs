// Time O(n)
// Space O(n)

public class Solution
{
    public bool IsValid(string s)
    {
        Dictionary<char, char> dict =
            new()
            {
                { '(', ')' },
                { '{', '}' },
                { '[', ']' }
            };

        Stack<char> stack = new();

        for (int i = 0; i < s.Length; i++)
        {
            if (dict.ContainsKey(s[i]))
                stack.Push(dict[s[i]]);
            else if (stack.Count > 0 && stack.Peek() == s[i])
                stack.Pop();
            else
                return false;
        }
        return stack.Count == 0;
    }
}
