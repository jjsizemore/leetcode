// Use a hashmap to associate element values with their frequency
// Add the pairs from the hashmap into a priority queue where frequency is negated so that we dequeue highest frequency first
// Create an array of size k
// Iterate from 0 to k - 1, adding elements from the priority queue to the array
// Return the array

// O(N) Time & O(N + k) Space where N is the number of elements in nums


public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var dict = new Dictionary<int, int>();

        // O(N) time
        foreach (int num in nums)
        {
            if (!dict.ContainsKey(num))
            {
                dict.Add(num, 1);
            }
            else
            {
                dict[num]++;
            }
        }

        // Creates heap of size k with custom comparer that results in non decreasing order
        var heap = new PriorityQueue<int, int>(k, Comparer<int>.Create((val1, val2) => val2 - val1));

        // O(Nlogk) time -- enqueueing N elements at logk time each
        foreach (var pair in dict)
        {
            heap.Enqueue(pair.Key, pair.Value);
        }

        var retVal = new int[k];

        // O(klogk) time
        for (int i = 0; i < k; i++)
        {
            retVal[i] = heap.Dequeue();
        }

        return retVal;
    }
}
