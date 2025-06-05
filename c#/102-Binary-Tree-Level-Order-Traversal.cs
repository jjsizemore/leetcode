#region Breadth First Search
public class Solution {
    public List<List<int>> LevelOrder(TreeNode root) {
        var retVal = new List<List<int>>();
        if (root == null) return retVal;

        var q = new Queue<TreeNode>();
        q.Enqueue(root);

        while (q.Count > 0) {
            var level = new List<int>();
            int levelCount = q.Count;

            for (int i = 0; i < levelCount; i++) {
                var cur = q.Dequeue();

                if (cur.left != null) q.Enqueue(cur.left);
                if (cur.right != null) q.Enqueue(cur.right);

                level.Add(cur.val);
            }

            retVal.Add(level);
        }

        return retVal;
    }
}

#endregion

#region Depth First Search
public class Solution {
    public List<List<int>> res = new List<List<int>>();

    public List<List<int>> LevelOrder(TreeNode root) {
        dfs(root, 0);
        return res;
    }

    private void dfs(TreeNode node, int depth) {
        if (node == null) {
            return;
        }

        if (res.Count == depth) {
            res.Add(new List<int>());
        }

        res[depth].Add(node.val);

        dfs(node.left, depth + 1);
        dfs(node.right, depth + 1);
    }
}

#endregion