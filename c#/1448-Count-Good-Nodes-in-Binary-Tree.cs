#region
/// <summary>
/// 1448. Count Good Nodes in Binary Tree
/// https://leetcode.com/problems/count-good-nodes-in-binary-tree/
///
/// Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
/// Return the number of good nodes in the binary tree.
///
/// Example 1:
/// Input: root = [3,1,4,3,null,1,5]
/// Output: 4
///
/// Example 2:
/// Input: root = [3,3,null,4,2]
/// Output: 3
///
/// Example 3:
/// Input: root = [1]
/// Output: 1
///
/// DFS with a helper function to keep track of the highest value seen so far.
/// If the current node's value is greater than or equal to the highest value seen so far,
/// then it is a good node.
/// We then update the highest value seen so far to the current node's value and continue
/// the DFS.
/// </summary>
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
#endregion