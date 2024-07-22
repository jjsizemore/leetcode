// Time O(1) -- always 32 bits
// Space O(1)
public class Solution
{
    public uint ReverseBits(uint n)
    {
        uint retVal = 0;
        for (int i = 0; i < 32; i++)
        {
            var bit = (n >> i) & 1;
            retVal = retVal | (bit << (31 - i));
        }
        return retVal;
    }
}
