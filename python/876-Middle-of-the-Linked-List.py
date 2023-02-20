# region Two Pointers
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Two Pointers

        - Time O(n)
        - Space O(1)
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# endregion
