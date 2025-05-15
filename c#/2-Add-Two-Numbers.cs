#region Iterative Solution
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

// Time: O(n + m)
// Space: O(1)
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        var dummy = new ListNode();
        var cur = dummy;

        while (l1 != null || l2 != null || carry != 0)
        {
            var val1 = l1?.val ?? 0;
            var val2 = l2?.val ?? 0;
            cur.next = new ListNode((val1 + val2 + carry) % 10);
            carry = (int)Math.Floor((decimal)((val1 + val2 + carry) / 10));
            cur = cur.next;
            l1 = l1?.next;
            l2 = l2?.next;
        }

        return dummy.next;
    }
}
#endregion