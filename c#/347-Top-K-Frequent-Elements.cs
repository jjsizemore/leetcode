#region Buckets

// Create an array of lists with size of nums
// Each index in the array will represent a frequency, and each list will have all elems with that frequency
// Use a hash map to get the frequencies, add the elements to their frequency buckets
// Iterate backwards through the buckets and add them to the return array until we have k elems

// O(N) Time and O(N) Space

public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var dict = new Dictionary<int, int>();

        foreach (int num in nums)
            if (!dict.TryAdd(num, 1)) dict[num]++;

        // must be 1 greater than size of array since if all elems are the same,
        // count would be N but last index in nums is N-1
        var buckets = new List<int>[nums.Length + 1];

        for (int i = 0; i < buckets.Length; i++) buckets[i] = new List<int>();

        foreach (var pair in dict) buckets[pair.Value].Add(pair.Key);

        var retVal = new int[k];
        int addedCounter = 0;
        for (int j = buckets.Length - 1; j >= 0; j--)
        {
            foreach (int num in buckets[j])
            {
                if (addedCounter >= k)
                    break;
                retVal[addedCounter++] = num;
            }
        }

        return retVal;
    }
}

#endregion Buckets

#region QuickSelect
// This solution uses the quicksort algorithm
// After creating an ascending sorted array, the pivot will be such that all elements on the left
// are less frequent, and all elements on the right are at least as frequent
// Choose a random pivot
// If the pivot is the N - k position, then the elements to the right including the pivot are the k most frequent elements
// If not, we can choose the pivot again until it's in the right position

// O(N) average time complexity -- can be as bad as O(N^2) if we pick the worst pivot every time,
// but the chances of this happening with randomly selected pivots is very low. Could also use middle.
// If we partition into arrays of size 1 and n - 1 every time, we'd have O(N^2)

// O(N) space for the dict and the unique array

public class Solution {

    private Dictionary<int, int> _dict;
    private int[] _unique;

    public int[] TopKFrequent(int[] nums, int k) {
        _dict = new Dictionary<int, int>();

        // Creating map of all values to their frequencies
        foreach (int num in nums)
        {
            if (!_dict.TryAdd(num, 1)) _dict[num]++;
        }

        // Create an array of unique values based on the keys in the dict
        int n = _dict.Count;
        _unique = new int[n];

        int i = 0;
        foreach (var key in _dict.Keys)
        {
            _unique[i++] = key;
        }

        // We want to do a partial sort on the unique array so that all elements up to
        // the (N-k)th least frequent element are to the left,
        // then the elements in the unique array N-k onward are the k most frequent
        quickSelect(0, n - 1, n - k);

        return _unique[(n - k)..];
    }

    // kSmallest is the number of elements that we need to be smaller than the pivot
    // This value will be N - k here so that the remaining k elements on the right are
    // the k highest frequency
    public void quickSelect(int left, int right, int kSmallest)
    {
        // base case -- list only contains one element
        if (left == right) return;

        var rand = new Random();

        int pivotIdx = left + rand.Next(right - left);
        // int pivotIdx = left + (right - left) / 2;

        pivotIdx = partition(left, right, pivotIdx);

        if (pivotIdx == kSmallest)
            return;
        else if (pivotIdx > kSmallest)
            // move pivot left
            quickSelect(left, pivotIdx - 1, kSmallest);
        else
            // move pivot right
            quickSelect(pivotIdx + 1, right, kSmallest);
    }

    // Moves pivot to the end of the partition
    // Moves all less frequent elements than pivot to the left
    // Moves the pivot to its final location within the partition, so that all elems left of it are less frequent
    // and all elems to the right of it are greater than it
    // Returns the final location of the pivot
    public int partition(int left, int right, int pivotIdx)
    {
        int pivotValue = _unique[pivotIdx];
        int pivotFreq = _dict[pivotValue];

        // move pivot to end
        swap(pivotIdx, right);
        int storeIdx = left;

        // move all less frequent elements to the left
        for (int i = left; i <= right; i++)
        {
            if (_dict[_unique[i]] < pivotFreq)
            {
                swap(storeIdx++, i);
            }
        }

        swap(storeIdx, right);

        return storeIdx;
    }

    // Swaps values within the unique array at indices x and y
    public void swap(int x, int y)
    {
        int tmp = _unique[x];
        _unique[x] = _unique[y];
        _unique[y] = tmp;
    }
}

#endregion QuickSelect

#region HeapSolution

// Use a hashmap to associate element values with their frequency
// Add the pairs from the hashmap into a priority queue where frequency is negated so that we dequeue highest frequency first
// Create an array of size k
// Iterate from 0 to k - 1, adding elements from the priority queue to the array
// Return the array

// O(Nlogk) Time & O(N + k) Space where N is the number of elements in nums


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

#endregion HeapSolution
