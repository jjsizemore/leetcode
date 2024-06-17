// Use helper function to recursively find max depth so far (global var) and add values with depths to a global queue
// Iterate through the elements in the queue and find weighted sum using the maxDepth value
// Return the weighted sum

// O(N) Time where N is number of elements in the list
// O(N) Space. Callstack max is O(D) where D is max depth

public class Solution
{
    private Queue<List<int>> _valuesAndDepths = new Queue<List<int>>();

    private int _maxDepth = 0;

    private void helper(IList<NestedInteger> nestedList, int depth)
    {
        _maxDepth = Math.Max(depth, _maxDepth);

        foreach (var nestedInt in nestedList)
        {
            if (nestedInt.IsInteger())
            {
                _valuesAndDepths.Enqueue(new List<int> { nestedInt.GetInteger(), depth });
            }
            else
            {
                helper(nestedInt.GetList(), depth + 1);
            }
        }
    }

    public int DepthSumInverse(IList<NestedInteger> nestedList)
    {
        helper(nestedList, 1);

        int weightSum = 0;

        while (_valuesAndDepths.Count > 0)
        {
            var valueAndDepth = _valuesAndDepths.Dequeue();
            weightSum += valueAndDepth[0] * (_maxDepth - valueAndDepth[1] + 1);
        }

        return weightSum;
    }
}
