public class Solution {
    public class Edge {
        public int p1;
        public int p2;
        public int cost;

        public Edge(int p1, int p2, int cost) {
            this.p1 = p1;
            this.p2 = p2;
            this.cost = cost;
        }
    }

    public class DSU {
        public int[] Parent, Size;

        public DSU(int n) {
            Parent = new int[n];
            Size = new int[n];

            for (int i = 0; i < n; i++) {
                Parent[i] = i;
            }
            Array.Fill(Size, 1);
        }

        public int Find(int node) {
            if (Parent[node] != node) {
                Parent[node] = Find(Parent[node]);
            }
            return Parent[node];
        }

        public bool Union(int u, int v) {
            int pu = Find(u);
            int pv = Find(v);
            if (pu == pv) return false;
            if (Size[pu] < Size[pv]) {
                // swap parents so u has the bigger group
                int tmp = pu;
                pu = pv;
                pv = tmp;
            }
            // u eats v
            Size[pu] += Size[pv];
            Parent[pv] = pu;
            return true;
        }
    }

    public int MinCostConnectPoints(int[][] points) {
        int n = points.Length;
        DSU dsu = new DSU(n);

        var edges = new List<Edge>();
        // Step 1: Create edges between all points
        for (int i = 0; i < points.Length; i++) {
            for (int j = i + 1; j < points.Length; j++) {
                int cost = Math.Abs(points[i][0] - points[j][0]) +
                    Math.Abs(points[i][1] - points[j][1]);
                edges.Add(new Edge(i, j, cost));
            }
        }

        // Step 2: Sort them by manhattan dist
        edges.Sort((a, b) => a.cost - b.cost);

        // Step 3: Traverse edges to connect nodes and add to final weight if edge is added
        int totalCost = 0;
        int totalEdges = 0;

        foreach (var edge in edges) {
            if (dsu.Union(edge.p1, edge.p2)) {
                totalCost += edge.cost;
                totalEdges += 1;

                // MST has n - 1 edges
                if (totalEdges == n - 1) {
                    break;
                }
            }
        }

        return totalCost;
    }
}
