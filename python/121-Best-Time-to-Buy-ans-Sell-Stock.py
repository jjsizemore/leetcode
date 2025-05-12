class Solution:
    # Time O(n)
    # Space O(1)
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestPrice = prices[0]

        for price in prices:
            maxProfit = max(maxProfit, price - lowestPrice)
            lowestPrice = min(price, lowestPrice)

        return maxProfit
