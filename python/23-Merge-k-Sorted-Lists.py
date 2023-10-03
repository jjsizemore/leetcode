import heapq
from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# region HeapQ
# Time O(Nlogk) -- Comparison cost will be length of heap, k. N comparisons
# Space O(N) -- new linked list costs N. heap will be O(k) but this will usually be far less than N


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        h = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        while h:
            val, i = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        return dummy.next


# endregion

# region Simpler but less efficient HeapQ

# Somewhat simpler heapq code but not as efficient
# Time O(NlogN) -- comparison cost is log of length of heap, which at worst is N
# Space O(N) -- new linked list costs O(N), prio Q also costs O(N)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        h = []

        for i in range(len(lists)):
            while lists[i]:
                heapq.heappush(h, lists[i].val)
                lists[i] = lists[i].next

        while h:
            val = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next


# endregion
