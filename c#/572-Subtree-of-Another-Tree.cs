#region Depth First Search (DFS)
// Time: O(m * n)
// Space: O(m + n)
// where m is the number of nodes in root and n is the number of nodes in subRoot
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public bool sameTree(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return true;
        if (root1 == null || root2 == null) return false;
        if (root1.val != root2.val) return false;

        return sameTree(root1.left, root2.left) && sameTree(root1.right, root2.right);
    }

    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        // Subproblem: check if 2 trees are identical
        //      every node in both trees has same value and structure
        // Return true if subproblem is true for root or any children of root
        if (root == null) return false;

        return sameTree(root, subRoot) ||
               IsSubtree(root.left, subRoot) ||
               IsSubtree(root.right, subRoot);
    }
}
#endregion