class UnionFind:
    """A data structure to efficiently manage a collection of disjoint sets."""
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        """Finds the root of the set that contains node."""
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        """Unites the sets that contain node1 and node2."""
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1

def kruskals_algorithm_k_trees(edges, n, k):
    """
    Uses Kruskal's algorithm to find a minimum spanning forest with exactly k trees.
    :param edges: A list of tuples (u, v, weight) representing the edges of the graph.
    :param n: The number of vertices in the graph.
    :param k: The desired number of trees in the forest.
    :return: Edges included in the minimum spanning forest.
    """
    edges.sort(key=lambda edge: edge[2])
    uf = UnionFind(n)
    forest = []

    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            forest.append((u, v, w))
            if len(set(uf.find(i) for i in range(n))) == k:
                break

    return forest

# Example usage
if __name__ == "__main__":
    edges = [(0, 1, 2), (0, 2, 3), (1, 2, 4), (2, 3, 1), (3, 4, 5)]
    vertices = 5
    k = 2  # Specify the number of trees (k)
    result = kruskals_algorithm_k_trees(edges, vertices, k)
    print("Edges in the forest:", result)
