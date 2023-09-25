from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        dGas = [gas[i] - cost[i] for i in range(N)]

        if sum(dGas) < 0:
            return -1

        minSeen = 0
        curSum = 0
        retVal = 0
        for i in range(N):
            curSum += dGas[i]
            if curSum < minSeen:
                minSeen = curSum
                retVal = (i + 1) % N
        return retVal
