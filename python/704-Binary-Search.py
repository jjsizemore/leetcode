class Solution:
    # Space O(1)
    # Time O(logn)
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while (i <= j):
            mid = math.floor(j + (i - j)/ 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return -1


