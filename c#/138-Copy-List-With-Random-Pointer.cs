/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;

    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/


// Create new linkedList nodes iteratively
// Inject new nodes into original linkedList, so that order is maintained for next step
// Iterate through combined list and use old nodes' .next.random values to set the new nodes' random values to the corresponding new random node
// Separate the new Nodes and the old nodes into their own linkedlists

public class Solution
{
    public Node CopyRandomList(Node head)
    {
        if (head == null)
            return head;

        var cur = head;

        // Inject new Nodes into linkedList, maintaining order
        while (cur != null)
        {
            var newNode = new Node(cur.val);
            var oldNext = cur.next;
            cur.next = newNode;
            newNode.next = oldNext;
            // Iterate to next old node
            cur = cur.next.next;
        }

        cur = head;

        // Set new nodes' random pointers
        while (cur != null)
        {
            cur.next.random = cur.random?.next;
            cur = cur.next.next;
        }

        var retVal = head.next;
        // Separate the new linkedList from the old linkedList
        while (head != null)
        {
            var newNodePtr = head.next;
            head.next = newNodePtr.next;
            newNodePtr.next = head.next?.next;
            head = head.next;
        }

        return retVal;
    }
}
