#region DFS
/// <summary>
/// LC 100: Same Tree
/// https://leetcode.com/problems/same-tree/
/// Approach: Recursive DFS
/// Time: O(n) - n is the number of nodes in the tree
/// Space: O(h) - h is the height of the tree
///  Best Case (Balanced Tree): O(log(n))
///  Worst Case (Skewed Tree): O(n)
/// </summary>
public class Solution {
    public bool IsSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;

        return p.val == q.val &&
                IsSameTree(p.left, q.left) &&
                IsSameTree(p.right, q.right);

    }
}
#endregion