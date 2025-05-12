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

public class Solution {
    public void ReorderList(ListNode head) {
        if (head?.next == null) return;

        // Step 1: Find middle
        var slow = head;
        var fast = head.next;

        while (fast?.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Step 2: Reverse second half
        var second = slow.next;
        slow.next = null;
        ListNode prev = null;

        while (second != null)
        {
            var next = second.next;
            second.next = prev;
            prev = second;
            second = next;
        }


        // Step 3: Merge lists
        var first = head;
        second = prev;
        while (second != null)
        {
            var temp1 = first.next;
            var temp2 = second.next;
            first.next = second;
            second.next = temp1;
            first = temp1;
            second = temp2;
        }
    }
}
