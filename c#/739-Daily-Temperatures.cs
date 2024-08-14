#region Monotonic Stack
// Time O(n)
// Space O(n)
public class Solution
{
    public int[] DailyTemperatures(int[] temperatures)
    {
        // Create a stack that will hold temps and their indices [temp, idx]
        // Create a int[] res that will hold the returned value
        // Iterate through the temperature array
        //  While stack.Count > 0 & stack.Peek()[0] < temperatures[i]
        //      Pop the pair from the top of the stack to a ptr
        //      Set res[pair[1]] = i - pair[1]
        //  After while condition, add [temperatures[i], i] to stack
        // Return res
        Stack<int[]> stack = new();
        int[] res = new int[temperatures.Length];

        for (int i = 0; i < temperatures.Length; i++)
        {
            int temp = temperatures[i];

            while (stack.Count > 0 && temp > stack.Peek()[0])
            {
                int[] pair = stack.Pop();
                res[pair[1]] = i - pair[1];
            }
            stack.Push(new int[] { temp, i });
        }
        return res;
    }
}

#endregion
