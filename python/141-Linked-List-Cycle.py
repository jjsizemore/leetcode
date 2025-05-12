# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# region Floyd's Cycle Finding Algorithm (slow/fast pointers)


class Solution:
    # Space O(1)
    # Time O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


# endregion


# region Hash Table / Set Solution
class Solution:
    # Space O(n)
    # Time O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mySet = set()
        while head is not None:
            if head in mySet:
                return True
            else:
                mySet.add(head)
                head = head.next
        return False


# endregion
