#region MinHeap
/// <summary>
/// 703. Kth Largest Element in a Stream
/// https://leetcode.com/problems/kth-largest-element-in-a-stream/
///
/// Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
///
/// Implement KthLargest class:
/// KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
/// int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
///
/// Example 1:
/// Input
/// ["KthLargest", "add", "add", "add", "add", "add"]
/// [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
/// Output
/// [null, 4, 5, 5, 8, 8]
///
/// Explanation
/// KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
/// kthLargest.add(3);   // return 4
/// kthLargest.add(5);   // return 5
/// kthLargest.add(10);  // return 5
/// kthLargest.add(9);   // return 8
/// kthLargest.add(4);   // return 8
///
///
///
///
///
/// MinHeap is a good data structure for this problem because we can keep track of the kth largest element by removing all but k elements.
/// The element at idx 0 will be the kth largest element.
///
/// We can use a PriorityQueue to implement the MinHeap.
///
/// Time: O(m * log(k)) where m is the number of calls to add
/// Space: O(k)
///
///
///
///
///
///
///
/// </summary>
public class KthLargest {
    // Can use a MinHeap
    // Remove all but k elems, and elem at idx 0 will be kth largest

    private PriorityQueue<int, int> pq;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.pq = new();
        this.k = k;

        foreach (int num in nums) {
            pq.Enqueue(num,num);
            if (pq.Count > k) pq.Dequeue();
        }
    }

    public int Add(int val) {
        pq.Enqueue(val, val);

        if (pq.Count > k) pq.Dequeue();

        return pq.Peek();
    }
}

#endregion