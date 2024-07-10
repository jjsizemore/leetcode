#region 2 Pointers
// Time 	O(n)
// Space 	O(1)
public class Solution
{
    public bool HasCycle(ListNode head)
    {
        if (head == null)
            return false;

        ListNode fast = head.next;
        ListNode slow = head;

        while (fast != null && fast.next != null)
        {
            if (fast == slow)
                return true;
            fast = fast.next.next;
            slow = slow.next;
        }

        return false;
    }
}
#endregion


#region Set
// Time 	O(n)
// Space 	O(n)
public class Solution
{
    public bool HasCycle(ListNode head)
    {
        if (head == null)
            return false;

        HashSet<ListNode> seen = new();

        while (head != null)
        {
            if (seen.Contains(head))
                return true;
            seen.Add(head);
            head = head.next;
        }

        return false;
    }
}
#endregion
// Definition for a singly-linked list.
public class ListNode
{
    public int val;
    public ListNode next;

    public ListNode(int x)
    {
        val = x;
        next = null;
    }
}
