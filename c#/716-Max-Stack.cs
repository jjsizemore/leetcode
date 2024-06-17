// We can achieve the required functionality by maintaining two stacks
// One stack will function normally as a typical stack and handle the regular functions
// Another stack will exclusivly track maxes so far

// O(N) Time for PopMax(), O(1) for all others
// O(N) Space where N is total elems added

public class MaxStack
{
    private Stack<int> _stack;
    private Stack<int> _maxStack;

    public MaxStack()
    {
        _stack = new Stack<int>();
        _maxStack = new Stack<int>();
    }

    public void Push(int x)
    {
        _stack.Push(x);
        int max = _maxStack.Count > 0 ? _maxStack.Peek() : int.MinValue;
        _maxStack.Push(Math.Max(x, max));
    }

    public int Pop()
    {
        _maxStack.Pop();
        return _stack.Pop();
    }

    public int Top()
    {
        return _stack.Peek();
    }

    public int PeekMax()
    {
        return _maxStack.Peek();
    }

    public int PopMax()
    {
        // Create a buffer that will hold elements that are on top of the max element in the regular stack
        // Pop elems from the regular stack and the max stack until we see the top max elem in the reg stack
        // Add elems from the buffer to the regular stack again and add the max elem in the max stack to the max stack for each elem in the buffer

        var buffer = new Stack<int>();

        int max = PeekMax();

        while (Top() != max)
        {
            buffer.Push(Pop());
        }
        // Remove the max element
        Pop();

        while (buffer.Count > 0)
        {
            Push(buffer.Pop());
        }

        return max;
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.Push(x);
 * int param_2 = obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.PeekMax();
 * int param_5 = obj.PopMax();
 */
