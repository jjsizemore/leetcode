// Create a class called double linked node that has references to next and previous nodes
// Add pseudo head and tail values to the linkedList to make it easier to add and remove nodes
// Add DoubleLinkedNode helper methods such as:
// addNode (always adds to front)
// removeNode (removes a specific node object from the list)
// popTail (removes last node and returns the node object)
// moveToFront (calls removeNode() on the node object and then addNode() ot add node back to front)


// DOUBLE LINKED LIST + HASH MAP Solution
// O(1) Time, O(capacity) Space
public class LRUCache
{
    public class DoubleLinkedNode
    {
        public int key;
        public int value;
        public DoubleLinkedNode prev;
        public DoubleLinkedNode next;
    }

    private void addNode(DoubleLinkedNode node)
    {
        _head.next.prev = node;
        node.next = _head.next;
        _head.next = node;
        node.prev = _head;
    }

    private void removeNode(DoubleLinkedNode node)
    {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private DoubleLinkedNode popTail()
    {
        var lastNode = _tail.prev;
        removeNode(lastNode);

        return lastNode;
    }

    private void moveToFront(DoubleLinkedNode node)
    {
        removeNode(node);
        addNode(node);
    }

    private DoubleLinkedNode _head;
    private DoubleLinkedNode _tail;
    private int _capacity;
    private int _count;
    private Dictionary<int, DoubleLinkedNode> dict;

    public LRUCache(int capacity)
    {
        _head = new DoubleLinkedNode();
        _tail = new DoubleLinkedNode();
        _head.next = _tail;
        _tail.prev = _head;

        _capacity = capacity;
        _count = 0;

        dict = new Dictionary<int, DoubleLinkedNode>();
    }

    public int Get(int key)
    {
        if (dict.ContainsKey(key))
        {
            var node = dict[key];
            moveToFront(node);
            return node.value;
        }
        else
        {
            return -1;
        }
    }

    public void Put(int key, int value)
    {
        if (!dict.ContainsKey(key))
        {
            var newNode = new DoubleLinkedNode();
            newNode.key = key;
            newNode.value = value;
            addNode(newNode);
            dict[key] = newNode;
            if (dict.Count > _capacity)
            {
                var removedNode = popTail();
                dict.Remove(removedNode.key);
                Console.WriteLine(dict.Count);
            }
        }
        else
        {
            var existingNode = dict[key];
            moveToFront(existingNode);
            existingNode.value = value;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */
