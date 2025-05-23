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
    public int count = 0;

    public int GoodNodes(TreeNode root) {
        void helper (TreeNode root, int highest)
        {
            if (root == null)
            {
                return;
            }
            else if (root.val >= highest)
            {
                count += 1;
            }

            highest = Math.Max(root.val, highest);
            helper(root.left, highest);
            helper(root.right, highest);
        }

        helper(root, root.val);
        return count;
    }
}
