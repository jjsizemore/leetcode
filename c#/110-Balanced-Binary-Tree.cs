#region DFS
// Time O(n) - n is the number of nodes in the tree
// Space O(h) - h is the height of the tree
//  Best Case (Balanced Tree): O(log(n))
//  Worst Case (Skewed Tree): O(n)
public class Solution {
    public bool IsBalanced(TreeNode root) {
        return GetDepth(root) != -1;
    }

    public int GetDepth(TreeNode root) {
        if (root == null) return 0;

        int leftD = GetDepth(root.left);
        if (leftD == -1) {
            return -1;
        }

        int rightD = GetDepth(root.right);
        if (rightD == -1) {
            return -1;
        }

        if (Math.Abs(leftD - rightD) > 1) {
            return -1;
        }

        return Math.Max(leftD, rightD) + 1;
    }
}
#endregion

// Time		O(n*log(n))
// Space	O(N)
public class Solution
{
    public bool IsBalanced(TreeNode root)
    {
        if (root == null)
        {
            return true;
        }
        else if (Math.Abs(Measure(root.left) - Measure(root.right)) < 2)
        {
            return IsBalanced(root.left) && IsBalanced(root.right);
        }
        return false;
    }

    public int Measure(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        return 1 + Math.Max(Measure(root.left), Measure(root.right));
    }
}

//   Definition for a binary tree node.
public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
