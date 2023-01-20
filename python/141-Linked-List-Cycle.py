# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
  # Space O(n)
  # Time O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mySet = set()
        while head != None:
            if head in mySet:
                return True
            else:
                mySet.add(head)
                head = head.next
        return False
