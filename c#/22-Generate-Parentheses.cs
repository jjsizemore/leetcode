#region Backtracking w/ String Concat
// Time O(n)
// Space O(n)
public class Solution
{
    public List<string> GenerateParenthesis(int n)
    {
        // If openers is less than n, can add another opener
        // If closers is less than openers, can add another closer
        // Can use backtracking method to add all the possibilities to a list
        // We can just concat a string instead of building a stack with backtracking

        List<string> res = new();
        Backtrack(n, 0, 0, "", res);
        return res;

        void Backtrack(int n, int nOpen, int nClose, string seq, IList<string> res)
        {
            if (nOpen == n && nClose == n)
            {
                res.Add(seq);
                return;
            }

            if (nOpen < n)
            {
                Backtrack(n, nOpen + 1, nClose, seq + "(", res);
            }
            if (nClose < nOpen)
            {
                Backtrack(n, nOpen, nClose + 1, seq + ")", res);
            }
        }
    }
}

#endregion
