# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        left, right = dummy, dummy

        for _ in range(n + 1):
            right = right.next

        while right is not None:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
