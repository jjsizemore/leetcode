import heapq
from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# region Divide and Conquer
# Time: O(Nlogk) where k is num of linked lists
#   Can merge two sorted lists in O(n) where n is num of nodes in the two lists
#   We do this process logk times, so the summation of all these nlogk is O(Nlogk)
# Space: O(1) -- we can merge two sorted linked lists in O(1) space


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numLists = len(lists)

        interval = 1

        while interval < numLists:
            for i in range(0, numLists - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if numLists else None

    def merge2Lists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ptr = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next

        ptr.next = l1 if l1 else l2

        return dummy.next


# endregion

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
