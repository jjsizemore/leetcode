public class Solution
{
    public string Encode(IList<string> strs)
    {
        var retVal = string.Concat(strs.Select(s => $"{s.Length}#{s}"));
        Console.WriteLine(retVal);
        return retVal;
    }

    public List<string> Decode(string s)
    {
        List<string> retVal = new();
        int start = 0;

        while (start < s.Length)
        {
            int end = start;

            while (s[end] != '#')
            {
                end++;
            }

            int.TryParse(s.Substring(start, end - start), out var len);

            start = end + 1;

            retVal.Add(s.Substring(start, len));

            start += len;
        }

        return retVal;
    }
}
