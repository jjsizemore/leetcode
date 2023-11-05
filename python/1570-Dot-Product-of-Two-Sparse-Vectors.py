# region Index-Value Pairs
# Time O(N); O(L_1 + L_2) where L_1 & L_2 are the number of nonzero elements
# Space O(L)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = []
        for idx, num in enumerate(nums):
            if num != 0:
                self.nonzeros.append((idx, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        result = 0
        p, q = 0, 0

        while p < len(self.nonzeros) and q < len(vec.nonzeros):
            if self.nonzeros[p][0] == vec.nonzeros[q][0]:
                result += self.nonzeros[p][1] * vec.nonzeros[q][1]
                p += 1
                q += 1
            elif self.nonzeros[p][0] < vec.nonzeros[q][0]:
                p += 1
            else:
                q += 1

        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
# endregion


# region HashMap
# Time O(N) for creating the hashmap, O(L) for the dot product, where L is the smaller number of nonzero elements
# Space O(L) for the hashmap
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.nonzeros[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        retVal = 0

        useSelf = len(self.nonzeros.items()) < len(vec.nonzeros.items())

        def helper(first, second):
            nonlocal retVal
            for idx, num in first.nonzeros.items():
                if idx in second.nonzeros:
                    retVal += num * second.nonzeros[idx]

        if useSelf:
            helper(self, vec)
        else:
            helper(vec, self)

        return retVal


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
# endregion
