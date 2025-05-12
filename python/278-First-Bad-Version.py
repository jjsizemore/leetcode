# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    # Space O(1)
    # Time O(logn)
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
