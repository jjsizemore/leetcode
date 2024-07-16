// Push: O(1)
// Pop: O(1) amortized -- generally will be O(1) unless qStack empty, then O(n)
// Peek: O(1) same as pop
// Empty: O(1)
public class MyQueue
{
    // Push: we can always push to same stack
    // Pop: we will rely on second stack to simulate a queue. if it's empty, pop all elems from push stack to queue stack. pop top of stack for first elem
    // Peek: peek is same as push except we peek first elem
    // Empty: true if both stack counts are 0

    Stack<int> pushStack;
    Stack<int> qStack;

    public MyQueue()
    {
        pushStack = new();
        qStack = new();
    }

    public void Push(int x)
    {
        pushStack.Push(x);
    }

    public int Pop()
    {
        PrepQueue();
        return qStack.Pop();
    }

    public int Peek()
    {
        PrepQueue();
        return qStack.Peek();
    }

    private void PrepQueue()
    {
        if (qStack.Count == 0)
        {
            while (pushStack.Count > 0)
                qStack.Push(pushStack.Pop());
        }
    }

    public bool Empty()
    {
        return qStack.Count == 0 && pushStack.Count == 0;
    }
}
