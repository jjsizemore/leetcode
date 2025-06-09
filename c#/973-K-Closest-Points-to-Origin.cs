#region Max Heap
/// <summary>
/// 973. K Closest Points to Origin
/// https://leetcode.com/problems/k-closest-points-to-origin/
///
/// Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
///
/// The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
///
/// You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
///
/// Example 1:
/// Input: points = [[1,3],[-2,2]], k = 1
/// Output: [[-2,2]]
/// Explanation:
/// The distance between (1, 3) and the origin is sqrt(10).
/// The distance between (-2, 2) and the origin is sqrt(8).
/// Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
/// We only want k = 1 points, so the answer is just [[-2,2]].
///
/// Example 2:
/// Input: points = [[3,3],[5,-1],[-2,4]], k = 2
/// Output: [[3,3],[-2,4]]
/// Explanation:
/// The answer [[-2,4],[3,3]] would also be accepted.
///
/// Constraints:
/// 1 <= k <= points.length <= 10^3
/// -100 < xi, yi < 100
/// </summary>
/// <remarks>
/// Time Complexity: O(n log k)
/// Space Complexity: O(k)
/// </remarks>
public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        // MaxHeap with -(dist to origin) as prio, removing if Count > k
        // Remaining k will be k pts with smallest dist to origin
        var maxHeap = new PriorityQueue<int[], int>();

        foreach (var coord in points) {
            int distSquared = coord[0] * coord[0] + coord[1] * coord[1];
            maxHeap.Enqueue(coord, -distSquared);

            if (maxHeap.Count > k) {
                maxHeap.Dequeue();
            }
        }

        var retVal = new int[k][];

        for (int i = 0; i < k; i++) {
            retVal[i] = maxHeap.Dequeue();
        }

        return retVal;
    }
}

#endregion