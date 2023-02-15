from typing import List

# region Dynamic Programming
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Dynamic Programming

        * Get max elevation seen from the left and right for each index
        * At each height except for the ends, subtract the cur height from the min of the left and right max elev values seen for that idx
        * If the diff is greater than 0 add it to the retVal

        Time O(n)
        Space O(n)
        """
        leftElev, rightElev = [0] * len(height), [0] * len(height)

        for i in range(1, len(height)):
            leftElev[i] = max(height[i - 1], leftElev[i - 1])
            j = len(height) - i - 1
            rightElev[j] = max(height[j + 1], rightElev[j + 1])

        retVal = 0
        for i in range(1, len(height) - 1):
            water = max(0, min(leftElev[i], rightElev[i]) - height[i])
            retVal += water
        return retVal


# endregion

# region Two Pointers
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two Pointers

        Start two pointers at either end of the array
        Util the pointers haven't passed each other, do the following:
          * Water is bound by the smaller of the two current values (leftCur and rightCur)
          * For the one which is smaller, compare it to the max seen for that side
          * If it's smaller than the max, add diff to the retVal and iterate the pointer toward the center

        Time O(n)
        Space O(1)

        """
        left, right = 0, len(height) - 1

        leftMax, rightMax = height[left], height[right]

        retVal = 0

        while left <= right:
            leftCur = height[left]
            rightCur = height[right]

            if leftCur < rightCur:
                leftMax = max(leftMax, leftCur)
                retVal += leftMax - leftCur
                left += 1
            else:
                rightMax = max(rightMax, rightCur)
                retVal += rightMax - rightCur
                right -= 1

        return retVal


# endregion
