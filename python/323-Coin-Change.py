import math
from typing import List
# region Bottom Up DP (Tabulation)
# Time O(len(coins) * amount)
# Space O(amount)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoinCounts = [math.inf] * (amount + 1)

        minCoinCounts[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                minCoinCounts[i] = min(
                    minCoinCounts[i], minCoinCounts[i - coin] + 1)
        return -1 if minCoinCounts[amount] == math.inf else minCoinCounts[amount]
# endregion

# region Top Down DP (Memoization)
# Time O(len(coins) * amount)
# Space O(amount)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(amtLeft, cache):
            if amtLeft < 0:
                return math.inf
            if amtLeft == 0:
                return 0
            if amtLeft in cache:
                return cache[amtLeft]

            cache[amtLeft] = min(
                helper(amtLeft - coin, cache) + 1 for coin in coins)
            return cache[amtLeft]

        retVal = helper(amount, {})
        return -1 if retVal == math.inf else retVal
# endregion
