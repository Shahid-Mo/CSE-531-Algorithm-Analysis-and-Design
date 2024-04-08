def bellman_ford(WList, source, end):
    """
    Finds the shortest path from source to all vertices in the graph using Bellman-Ford algorithm.
    :param WList: Adjacency list of the graph where keys are vertices and values are lists of tuples (neighbor, weight).
    :param source: The source vertex.
    :param end: The destination vertex.
    :return: The shortest distance to the destination vertex or 'INFINITY' if the vertex is unreachable.
    """
    infinity = float('inf')
    distance = {v: infinity for v in WList}
    distance[source] = 0
    
    for _ in range(len(WList) - 1):
        for u in WList:
            for v, d in WList[u]:
                if distance[u] + d < distance[v]:
                    distance[v] = distance[u] + d
    
    return distance[end] if distance[end] != infinity else 'INFINITY'

# Example of input handling and execution
if __name__ == "__main__":
    # Placeholder for input handling logic
    pass
