#region Iterative (2025 with top & bottom pointers)

/// <summary>
/// LC 235: Lowest Common Ancestor of a Binary Search Tree
/// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
/// Approach: Iterative
/// Time: O(N) -- in the case of a totally skewed tree where the LCA is second from leaf
/// Space: O(1)
/// </summary>
public class Solution {
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // can use binary search tree structure to speed things up
        // LCA if
        //  one target in one sub and (one in other or self)
        //  meaning (bot <= root && root <= top)

        var top = p.val > q.val ? p : q;
        var bot = top == p ? q : p;

        while (root != null) {
            if (top.val < root.val) {
                root = root.left;
            } else if (bot.val > root.val) {
                root = root.right;
            } else {
                return root;
            }
        }

        return null;
    }
}

#endregion

#region Iterative
/// <summary>
/// LC 235: Lowest Common Ancestor of a Binary Search Tree
/// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
/// Approach: Iterative
/// Time: O(N) -- in the case of a totally skewed tree where the LCA is second from leaf
/// Space: O(1)
/// </summary>
public class Solution
{
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
    {
        while (true)
        {
            if (root.val > p.val && root.val > q.val)
            {
                root = root.left;
            }
            else if (root.val < p.val && root.val < q.val)
            {
                root = root.right;
            }
            else
            {
                // If the root is neither bigger than both nor smaller than both,
                // it must either be between them or be one of the values.
                // In either case, it is the LCA
                return root;
            }
        }
    }
}

#endregion

#region Recursive

#endregion


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
