#region DFS (Instance Field Approach -- Object Oriented)
/// <summary>
/// LC 543: Diameter of Binary Tree
/// https://leetcode.com/problems/diameter-of-binary-tree/
/// Approach: Use instance field to track the max diameter
/// Time: O(n) - n is the number of nodes in the tree
/// Space: O(h) - h is the height of the tree
///  Best Case (Balanced Tree): O(log(n))
///  Worst Case (Skewed Tree): O(n)
/// </summary>
public class Solution {

    public int MaxD = 0;

    public int DiameterOfBinaryTree(TreeNode root) {
        GetDepth(root);
        return MaxD;
    }

    public int GetDepth(TreeNode node) {
        if (node == null) return 0;

        int lDepth = GetDepth(node.left);
        int rDepth = GetDepth(node.right);

        MaxD = Math.Max(MaxD, lDepth + rDepth);

        return Math.Max(lDepth, rDepth) + 1;
    }
}

#endregion

#region DFS (Ref Parameter Approach -- Functional (no side effects on class state))
/// <summary>
/// LC 543: Diameter of Binary Tree
/// https://leetcode.com/problems/diameter-of-binary-tree/
/// Approach: Use ref parameter to track the max diameter
/// Time: O(n) - n is the number of nodes in the tree
/// Space: O(h) - h is the height of the tree
///  Best Case (Balanced Tree): O(log(n))
///  Worst Case (Skewed Tree): O(n)
/// </summary>
public class Solution {
    public int DiameterOfBinaryTree(TreeNode root) {
        int MaxD = 0;
        GetDepth(root, ref MaxD);
        return MaxD;
    }

    public int GetDepth(TreeNode node, ref int MaxD) {
        if (node == null) return 0;

        int lDepth = GetDepth(node.left, ref MaxD);
        int rDepth = GetDepth(node.right, ref MaxD);

        MaxD = Math.Max(MaxD, lDepth + rDepth);

        return Math.Max(lDepth, rDepth) + 1;
    }
}

#endregion
