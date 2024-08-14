#region Stack
// Time O(n)
// Space O(n)
public class Solution
{
    public int EvalRPN(string[] tokens)
    {
        Stack<int> stack = new();

        foreach (string op in tokens)
        {
            if (op == "+")
            {
                stack.Push(stack.Pop() + stack.Pop());
            }
            else if (op == "-")
            {
                int second = stack.Pop();
                int first = stack.Pop();
                stack.Push(first - second);
            }
            else if (op == "*")
            {
                stack.Push(stack.Pop() * stack.Pop());
            }
            else if (op == "/")
            {
                int second = stack.Pop();
                int first = stack.Pop();
                stack.Push(first / second);
            }
            else
            {
                stack.Push(int.Parse(op));
            }
        }
        return stack.Pop();
    }
}

#endregion
