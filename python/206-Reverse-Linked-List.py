from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# region Recursive Solution


class Solution:
  # Space O(n)
  # Time O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(head, None)

    def helper(self, head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return prev
        else:
            nextHead = head.next
            head.next = prev
            return self.helper(nextHead, head)

# endregion

# region Iterative Solution


class Solution:
  # Space O(1)
  # Time O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None

        while head:
            ptr = head.next
            head.next = cur
            cur = head
            head = ptr

        return cur

# endregion
