# region DFS

from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjList = defaultdict(lambda: [])
        seen = set()

        for account in accounts:
            firstEmail = account[1]
            adjList[firstEmail].extend(account[2:])
            for email in account[2:]:
                adjList[email].append(firstEmail)

        def dfs(account, curList):
            seen.add(account)
            curList.append(account)
            for adjEmail in adjList[account]:
                if adjEmail not in seen:
                    dfs(adjEmail, curList)

        retVal = []

        for account in accounts:
            firstEmail = account[1]
            name = account[0]
            if firstEmail not in seen:
                curList = []
                dfs(firstEmail, curList)
                curList.sort()
                curList.insert(0, name)
                retVal.append(curList)

        return retVal


# endregion
