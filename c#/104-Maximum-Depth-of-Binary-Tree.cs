#region Recursive DFS
// Time O(n)
// Space O(h) where h is height of tree
public class Solution {
    public int MaxDepth(TreeNode root) {
        // base case null return 0
        if (root == null) return 0;

        // recurse return 1 + Max(MaxDepth(l), MaxDepth(r))
        return 1 + Math.Max(MaxDepth(root.left), MaxDepth(root.right));
    }
}

#endregion

#region Iterative BFS
// Time O(n)
// Space O(n)
// where n is number of nodes in tree
public class Solution {
    public int MaxDepth(TreeNode root) {
        if (root == null) return 0;

        int depth = 0;
        var q = new Queue<TreeNode>();
        q.Enqueue(root);

        while (q.Count > 0) {
            depth++;
            int levelSize = q.Count;

            for (int i = 0; i < levelSize; i++) {
                var cur = q.Dequeue();

                if (cur.left != null) q.Enqueue(cur.left);
                if (cur.right != null) q.Enqueue(cur.right);
            }
        }
        return depth;
    }
}

#endregion