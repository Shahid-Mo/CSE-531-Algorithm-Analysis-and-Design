import numpy as np

class Dijkstra:
    """
    A class to calculate the shortest path from a single source to all other vertices in a graph
    using Dijkstra's algorithm.
    """

    @staticmethod
    def shortest_path(graph, source):
        """
        Calculates the shortest path distances from `source` to all vertices in the graph.
        
        Parameters:
            graph: An instance of a Graph class which provides a get_matrix() method
                   that returns an adjacency matrix representing the graph.
            source (int): The index of the source vertex from which to calculate distances.
            
        Returns:
            A dictionary mapping each vertex to its shortest distance from the source.
        """
        matrix = graph.get_matrix()
        rows, cols, _ = matrix.shape
        infinity = np.inf
        visited = {v: False for v in range(rows)}
        distance = {v: infinity for v in range(rows)}
        distance[source] = 0

        for _ in range(rows):
            # Find the unvisited node with the smallest distance
            u = min((v for v in range(rows) if not visited[v]), key=lambda v: distance[v], default=None)
            if u is None:
                break
            visited[u] = True

            for v in range(cols):
                if matrix[u, v, 0] == 1 and not visited[v]:  # Edge exists and destination vertex not visited
                    alt = distance[u] + matrix[u, v, 1]  # Alternative path distance
                    if alt < distance[v]:  # If alternative path is shorter
                        distance[v] = alt

        return distance

# Example usage, use the Graph class instance `graph` from graph.py
if __name__ == "__main__":
    source_vertex = 0
    distances = Dijkstra.shortest_path(graph, source_vertex)
    print(f"Shortest distances from vertex {source_vertex}: {distances}")
