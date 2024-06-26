// Time		O(N) -- in the case of a totally skewed tree where the LCA is second from leaf
// Space	O(1)
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
