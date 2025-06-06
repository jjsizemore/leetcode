#region DFS
/// <summary>
/// 230. Kth Smallest Element in a BST
/// https://leetcode.com/problems/kth-smallest-element-in-a-bst/
///
/// Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
///
/// Example 1:
/// Input: root = [3,1,4,null,2], k = 1
/// Output: 1
///
/// Example 2:
/// Input: root = [5,3,6,2,4,null,null,1], k = 3
/// Output: 3
///
/// Constraints:
/// The number of nodes in the tree is n.
/// 1 <= k <= n <= 10^4
/// 0 <= Node.val <= 10^4
///
/// </summary>
/// <remarks>
/// Time Complexity: O(n)
/// Space Complexity: O(n)
/// </remarks>
public class Solution {
    private int count;
    private int retVal;

    public int KthSmallest(TreeNode root, int k) {
        // DFS - inorder traverse
        dfs(root, k);
        return this.retVal;
    }

    // returns true if node is found
    private bool dfs(TreeNode node, int k) {
        if (node == null) return false;

        if (dfs(node.left, k)) return true;

        count++;

        if (count == k) {
            retVal = node.val;
            return true;
        }

        return dfs(node.right, k);
    }
}

#endregion