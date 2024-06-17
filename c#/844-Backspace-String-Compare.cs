// Medium Solution
// Two pointers, walk through string backwards.
// O(1) Space, O(M + N) Time where M & N are respective lengths
public class Solution
{
    public bool BackspaceCompare(string s, string t)
    {
        int sPtr = s.Length - 1,
            tPtr = t.Length - 1;
        int sSkips = 0,
            tSkips = 0;

        while (sPtr >= 0 || tPtr >= 0)
        {
            while (sPtr >= 0)
            {
                if (s[sPtr] == '#')
                {
                    sSkips++;
                    sPtr--;
                }
                else if (sSkips > 0)
                {
                    sSkips--;
                    sPtr--;
                }
                else
                    break;
            }

            while (tPtr >= 0)
            {
                if (t[tPtr] == '#')
                {
                    tSkips++;
                    tPtr--;
                }
                else if (tSkips > 0)
                {
                    tSkips--;
                    tPtr--;
                }
                else
                    break;
            }

            // If we're in the middle of both strings, chars should be equal
            if (sPtr >= 0 && tPtr >= 0 && s[sPtr] != t[tPtr])
                return false;

            // Trying to compare char to null should end loop
            if ((sPtr >= 0) != (tPtr >= 0))
                return false;

            sPtr--;
            tPtr--;
        }

        return true;
    }
}

// Easy Solution
// Walk forward through strings and build new ones with backspaces applied, then compare
// O(M + N) Space, O(M + N) Time, where M & N are respective lengths

public class Solution
{
    private string applyBackspaces(string s)
    {
        var sb = new StringBuilder();

        foreach (var c in s)
        {
            if (c == '#' && sb.Length > 0)
                sb.Remove(sb.Length - 1, 1);
            else if (c != '#')
                sb.Append(c);
            Console.WriteLine(sb);
        }
        return sb.ToString();
    }

    public bool BackspaceCompare(string s, string t)
    {
        s = applyBackspaces(s);
        t = applyBackspaces(t);

        return string.Equals(s, t);
    }
}
