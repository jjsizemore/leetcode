// Time		O(n) - visiting each node once
// Space	O(log(n)) - height of tree O(H), could be O(n) in case of totally skewed tree

public class Solution
{
    public TreeNode InvertTree(TreeNode root)
    {
        if (root == null)
            return root;

        var ptr = InvertTree(root.left);
        root.left = InvertTree(root.right);
        root.right = ptr;

        return root;
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
