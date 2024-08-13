#region Two Stacks (Stack & Min Stack)
// Time O(n)
// Space O(n)
public class MinStack
{
    private Stack<int> _stack;
    private Stack<int> _minStack;

    public MinStack()
    {
        _stack = new();
        _minStack = new();
    }

    public void Push(int val)
    {
        _stack.Push(val);
        val = Math.Min(val, _minStack.Count == 0 ? val : _minStack.Peek());
        _minStack.Push(val);
    }

    public void Pop()
    {
        _stack.Pop();
        _minStack.Pop();
    }

    public int Top()
    {
        return _stack.Peek();
    }

    public int GetMin()
    {
        return _minStack.Peek();
    }
}

#endregion
