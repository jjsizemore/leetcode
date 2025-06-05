#region DFS
/// <summary>
/// 98. Validate Binary Search Tree
/// https://leetcode.com/problems/validate-binary-search-tree/
///
/// Given a binary tree, determine if it is a valid binary search tree (BST).
///
/// Assume a BST is defined as follows:
/// The left subtree of a node contains only nodes with keys less than the node's key.
/// The right subtree of a node contains only nodes with keys greater than the node's key.
/// Both the left and right subtrees must also be binary search trees.
///
/// Example 1:
/// Input: root = [2,1,3]
/// Output: true
///
/// Example 2:
/// Input: root = [5,1,4,null,null,3,6]
/// Output: false
///
/// Example 3:
/// Input: root = [1,1]
/// Output: false
///
/// </summary>
///
/// Time: O(n)
/// Space: O(n)
///
/// We can use a recursive helper function to track the bounds of the left and right subtrees.
///
///
public class Solution {
    // Seems like a recursive helper function would be needed to track bounds

    public bool IsValidBST(TreeNode root) {
        return IsValid(root);
    }

    public bool IsValid(TreeNode node, int? min = null, int? max = null) {
        if (node == null) return true;

        if ((min.HasValue && node.val <= min.Value) ||
            (max.HasValue && node.val >= max.Value)) {
                return false;
        }

        // val is max for left and min for right

        return IsValid(node.left, min, node.val) &&
                IsValid(node.right, node.val, max);
    }
}
#endregion