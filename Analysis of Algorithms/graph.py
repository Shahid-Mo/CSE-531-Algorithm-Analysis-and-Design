import numpy as np

class Graph:
    """
    A Graph class that uses an adjacency matrix to store edge weights and presence.
    
    Attributes:
        size (int): The number of vertices in the graph.
        matrix (np.array): A 3D NumPy array where each element [i, j] contains
                           [presence flag, weight] for the edge from vertex i to vertex j.
    
    Methods:
        __init__(edges, size): Constructs a Graph object given edges and size.
        get_matrix(): Returns the adjacency matrix of the graph.
    """
    
    def __init__(self, edges, size):
        """
        Initializes the Graph with vertices and edges.
        
        Parameters:
            edges (list of tuples): Each tuple represents an edge in the format (i, j, w),
                                    where 'i' is the start vertex, 'j' is the end vertex,
                                    and 'w' is the weight of the edge.
            size (int): The number of vertices in the graph.
        """
        self.size = size
        self.matrix = np.zeros((size, size, 2))
        
        for i, j, w in edges:
            self.matrix[i, j] = [1, w]  # Edge presence and weight from i to j
            # For undirected graphs, add the reverse edge
            self.matrix[j, i] = [1, w]  # Uncomment for undirected graphs

    def get_matrix(self):
        """
        Returns the adjacency matrix representing the graph.
        
        Returns:
            np.array: The graph's adjacency matrix.
        """
        return self.matrix

# Example usage
if __name__ == "__main__":
    edges = [(0, 1, 5), (1, 2, 3), (2, 0, 1), (1, 3, 10), (3, 2, 7)]
    size = 4
    graph = Graph(edges, size)
    
    print("Graph's adjacency matrix:")
    print(graph.get_matrix())
