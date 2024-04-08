import numpy as np

class WeightedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = np.zeros((num_vertices, num_vertices, 2))
    
    def add_edge(self, u, v, weight):
        """
        Adds a directed edge from vertex u to vertex v with the given weight.
        """
        self.matrix[u, v, 0] = 1  # Edge presence
        self.matrix[u, v, 1] = weight  # Edge weight

    def get_matrix(self):
        """
        Returns the adjacency matrix of the graph.
        """
        return self.matrix

    def bellman_ford(self, source):
        """
        Finds the shortest path from source to all vertices in the graph using the Bellman-Ford algorithm.
        """
        infinity = np.inf
        distance = {v: infinity for v in range(self.num_vertices)}
        distance[source] = 0

        for _ in range(self.num_vertices - 1):
            for u in range(self.num_vertices):
                for v in range(self.num_vertices):
                    if self.matrix[u, v, 0] == 1:  # If there's an edge
                        distance[v] = min(distance[v], distance[u] + self.matrix[u, v, 1])
        
        # Check for negative-weight cycles
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if self.matrix[u, v, 0] == 1 and distance[u] + self.matrix[u, v, 1] < distance[v]:
                    print("Graph contains a negative-weight cycle")
                    return None

        return distance

# Example usage
if __name__ == "__main__":
    graph = WeightedGraph(5)
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 2, 7)
    graph.add_edge(1, 3, 5)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 4, -4)
    graph.add_edge(2, 3, -3)
    graph.add_edge(2, 4, 9)
    graph.add_edge(3, 1, -2)
    graph.add_edge(4, 0, 2)
    graph.add_edge(4, 3, 7)
    
    distances = graph.bellman_ford(0)
    if distances:
        print("Shortest distances from source to all vertices:", distances)
