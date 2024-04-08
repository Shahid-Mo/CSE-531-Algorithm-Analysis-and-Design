from collections import deque

def bfs(graph, start):
    """
    Performs BFS traversal from a given start vertex.

    Parameters:
        graph (dict): A dictionary representing the adjacency list of the graph where keys are vertices
                      and values are lists of adjacent vertices.
        start: The vertex from which BFS traversal starts.
    """
    visited = set()  # A set to keep track of visited vertices
    queue = deque([start])  # A queue to manage the BFS traversal order

    while queue:
        vertex = queue.popleft()  # Dequeue a vertex from the queue
        if vertex not in visited:
            print(vertex, end=' ')  # Process the vertex (e.g., print it out)
            visited.add(vertex)  # Mark this vertex as visited
            # Enqueue all adjacent and unvisited vertices
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B', 'H'],
        'F': ['C'],
        'G': ['C'],
        'H': ['E']
    }
    print("BFS starting from vertex 'A':")
    bfs(graph, 'A')
