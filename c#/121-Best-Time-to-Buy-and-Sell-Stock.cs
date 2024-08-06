#region Two Pointers
// Time O(n)
// Space O(1)
public class Solution
{
    public int MaxProfit(int[] prices)
    {
        int least = prices[0],
            profit = 0;

        foreach (int price in prices)
        {
            least = Math.Min(least, price);
            profit = Math.Max(profit, price - least);
        }
        return profit;
    }
}

#endregion
#region Iterate Backwards
// Time 	O(n)
// Space 	O(1)
public class Solution
{
    public int MaxProfit(int[] prices)
    {
        // Iterate through array backwards
        // At each point, take max of max seen and cur, then subtract cur from max seen and take max of that value and max profit so far
        // Return max profit so far at end

        int cur,
            maxSeen,
            maxProfit;
        cur = maxSeen = maxProfit = 0;
        for (int i = prices.Length - 1; i >= 0; i--)
        {
            cur = prices[i];
            maxSeen = Math.Max(cur, maxSeen);
            maxProfit = Math.Max(maxSeen - cur, maxProfit);
        }

        return maxProfit;
    }
}
#endregion
