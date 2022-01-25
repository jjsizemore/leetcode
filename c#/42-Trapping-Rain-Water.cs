// Water is going to be bound by lower side
// If left height is less than right, water is bound by left, so calculate any trapped water & add to sum by subtracting curr left height from max left height, then iterate left ptr forward
// If right side is lower, do the above for right instead
// Once left > right, return sum

// TWO POINTER SOLUTION
// O(N) Time, O(1) Space

public class Solution {
    public int Trap(int[] height) {
        int left = 0, right = height.Length - 1;

        int leftMax = height[left], rightMax = height[right];

        int sum = 0;

        while (left <= right)
        {
            int leftCur = height[left];
            int rightCur = height[right];
            // Water is bound by left, calc water trapped by leftMax
            if (leftCur < rightCur)
            {
                leftMax = Math.Max(leftMax, leftCur);
                sum += leftMax - leftCur;
                left++;
            }
            else
            {
                rightMax = Math.Max(rightMax, rightCur);
                sum += rightMax - rightCur;
                right--;
            }
        }

        return sum;
    }
}
