from collections import defaultdict
import collections
from typing import List

# region Disjoint Set Union (DSU)

# Sets up accounts as groups of nodes represented by indices in the parents array
# Manages relationships between the groups by manipulating the parent values
class DSU:
    def __init__(self, size):
        self.parents = list(range(size))

    # Recursively find the parent node of the set
    def findRoot(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.findRoot(self.parents[x])
        return self.parents[x]

    # Set the parent of the root of the child equal to the root of the parent
    def union(self, child: int, parent: int) -> None:
        self.parents[self.findRoot(child)] = self.findRoot(parent)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Holds acct to parent group mapping
        accountMap = dict()

        dsu = DSU(len(accounts))

        for acctIdx, account in enumerate(accounts):
            for email in account[1:]:
                # If we've already seen the email, set cur acct group to have the same parent as the one the seen email is already associated with
                if email in accountMap:
                    dsu.union(acctIdx, dsu.findRoot(accountMap[email]))
                # We always set each email to map to its group -- this will be used to recursively find the email root group
                accountMap[email] = acctIdx

        retVal = collections.defaultdict(list)

        for email, parent in accountMap.items():
            retVal[dsu.findRoot(parent)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in retVal.items()]


# endregion

# region DFS


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
