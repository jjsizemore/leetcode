// For a triplet i,j,k to represent a triangle, i + j > k where i & j are both less than k
// Sort the elements in the array
// Use nested for loops to get pairs of numbers i & j
// For each pair, find the number of elements in the array that will satisfy the above condition,
// where the elements that can be k start after j

// O(N^2logN) Time where N is the number of elements. This is because we're performing binary search for N^2 pairs
// O(1) Space, unless you count space used to sort which is O(logN)

public class Solution
{
    private int[] _nums;

    public int TriangleNumber(int[] nums)
    {
        int count = 0;

        Array.Sort(nums);
        this._nums = nums;

        for (int i = 0; i < nums.Length - 2; i++)
        {
            // start index for largest number
            int k = i + 2;
            for (int j = i + 1; j < nums.Length - 1 && nums[i] != 0; j++)
            {
                // Will return the index of the first element that is bigger than or equal to nums[i] + nums[j]
                k = binarySearch(k, nums.Length - 1, nums[i] + nums[j]);
                count += (k - 1) - (j + 1) + 1;
            }
        }

        return count;
    }

    private int binarySearch(int left, int right, int max)
    {
        while (left <= right)
        {
            int mid = left + (right - left) / 2;

            // Eventually, the middle is going to be one less than the index of the max
            // This means that when we close the window and we have left = mid + 1, left will be index of the max
            if (_nums[mid] >= max)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }

        return left;
    }
}
