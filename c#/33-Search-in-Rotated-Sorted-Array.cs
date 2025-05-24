public class Solution {
    public int Search(int[] nums, int target) {
        int l = 0, r = nums.Length - 1;

        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (nums[mid] == target) return mid;

            // Step 1: Check which side is sorted
            if (nums[l] <= nums[mid]) {
                // Left side is sorted
                if (nums[l] <= target && target < nums[mid]) {
                    // target is left
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } else {
                // Right side is sorted
                if (nums[mid] < target && target <= nums[r]) {
                    // target is right
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }

        return -1;
    }
}
