#region Monotonic Queue
// Time O(n)
// Space O(n)
public class Solution
{
    public int[] MaxSlidingWindow(int[] nums, int k)
    {
        // Use monotonically decreasing deque. First value will always be max
        // When sliding window, remove value no longer in window, then
        //  check if last value of queue is smaller than new one, and remove until
        //  it's not or queue is empty.
        // Then take first value of queue for max at that window spot
        // Deque will contain indices of the values we care about
        int n = nums.Length;
        int[] res = new int[n - k + 1];

        LinkedList<int> q = new();
        int l = 0,
            r = 0;

        while (r < n)
        {
            while (q.Count > 0 && nums[q.Last.Value] < nums[r])
            {
                q.RemoveLast();
            }
            q.AddLast(r);

            if (l > q.First.Value)
            {
                q.RemoveFirst();
            }

            if (r - l + 1 == k)
            {
                res[l] = nums[q.First.Value];
                l++;
            }
            r++;
        }
        return res;
    }
}
#endregion
