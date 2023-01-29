# Space O(n)
# Time O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicesMap = {}
        for i, num in enumerate(nums):
            if target - num in indicesMap:
                return i, indicesMap[target - num]
            indicesMap[num] = i
