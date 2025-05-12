#region Two Pointers (1 pass)
// Time O(n)
// Space O(1)
public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        // Two Pointers (1 pass)

        // Use a dummy node to handle edge cases
        var dummy = new ListNode(0, head);
        var slow = dummy;
        var fast = dummy;

        // Move fast pointer n + 1 ahead
        for (int i = 0; i <= n; i++)
        {
            fast = fast.next;
        }

        // Iterate both pointers until fast = null
        while (fast != null)
        {
            slow = slow.next;
            fast = fast.next;
        }

        // Slow pointer will be pointing at node to remove
        slow.next = slow.next.next;

        return dummy.next;
    }
}
#endregion

#region Iteration (Two Pass)
// Time O(n)
// Space O(1)
public class Solution
{
    public ListNode RemoveNthFromEnd(ListNode head, int n)
    {
        // Dummy node simplifies edge cases
        var dummy = new ListNode(0, head);
        int len = 0;
        var cur = head;

        // Step 1: Find length
        while (cur != null)
        {
            cur = cur.next;
            len++;
        }

        // Step 2: Stop at node before nth from end
        cur = dummy;
        for (int i = 0; i < len - n; i++)
        {
            cur = cur.next;
        }

        // Step 3: Remove node and return head
        cur.next = cur.next.next;
        return dummy.next;
    }
}
#endregion