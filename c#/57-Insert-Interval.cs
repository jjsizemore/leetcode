// Time O(n)
// Space O(1)
public class Solution
{
    public int[][] Insert(int[][] intervals, int[] newInterval)
    {
        // Iterate through the intervals
        // If interval starts after new one, add new interval and add remaining intervals then return
        // If interval ends before new interval, add interval
        // Otherwise, edit newInterval start & end to be min & max of newInterval and current interval values
        // If we get out of the for loop, no intervals were after new one so we need to add newInterval

        List<int[]> retVal = new();

        for (int i = 0; i < intervals.Length; i++)
        {
            var interval = intervals[i];
            if (interval[0] > newInterval[1])
            {
                retVal.Add(newInterval);
                retVal.AddRange(intervals.Skip(i));
                return retVal.ToArray();
            }
            else if (interval[1] < newInterval[0])
            {
                retVal.Add(interval);
            }
            else
            {
                newInterval[0] = Math.Min(interval[0], newInterval[0]);
                newInterval[1] = Math.Max(interval[1], newInterval[1]);
            }
        }

        retVal.Add(newInterval);

        return retVal.ToArray();
    }
}
