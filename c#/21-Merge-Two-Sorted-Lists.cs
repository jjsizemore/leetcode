// Time 	O(n)
// Space 	O(n)
public class Solution
{
    public ListNode MergeTwoLists(ListNode list1, ListNode list2)
    {
        ListNode dummy = new();

        ListNode cur = dummy;
        while (list1 != null && list2 != null)
        {
            if (list1.val <= list2.val)
            {
                cur.next = list1;
                list1 = list1.next;
            }
            else
            {
                cur.next = list2;
                list2 = list2.next;
            }
            cur = cur.next;
        }

        if (list1 == null)
            cur.next = list2;
        else
            cur.next = list1;

        return dummy.next;
    }
}

/**
 * Definition for singly-linked list.
 */
public class ListNode
{
    public int val;
    public ListNode next;

    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}
