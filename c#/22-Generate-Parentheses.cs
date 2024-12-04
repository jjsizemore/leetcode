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

#region Backtracking w/ String Concat & Class Variable
public class Solution {
    private int n = 0;
    public List<string> GenerateParenthesis(int n) {
        // Can use backtracking
        // Valid strings must have opening parentheses before closing
        // If openers < n, can add opener
        // If closers < openers, can add closer

        n = n;
        var res = new List<string>();
        Helper(0, 0, "", res);

        return res;

        void Helper(int openers, int closers, string s, List<string> res) 
        {
            if (openers == n && closers == n)
            {
                res.Add(s);
                return;
            }

            if (openers < n)
            {
                Helper(openers + 1, closers, s + "(", res);
            }

            if (closers < openers)
            {
                Helper(openers, closers + 1, s + ")", res);
            }
        }
    }
}

#endregion