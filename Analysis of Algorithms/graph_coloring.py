def is_bipartite_graph(adj_list):
    """
    Determines if a graph is bipartite using graph coloring.
    :param adj_list: Dictionary representing the adjacency list of the graph.
    :return: True if the graph is bipartite, False otherwise.
    """
    vertex_color = {vertex: 'not colored' for vertex in adj_list}
    colors = ['red', 'blue']

    for start_vertex in adj_list:
        if vertex_color[start_vertex] == 'not colored':
            que = [start_vertex]
            vertex_color[start_vertex] = colors[0]
            while que:
                current_vertex = que.pop(0)
                for neighbor in adj_list[current_vertex]:
                    if vertex_color[neighbor] == 'not colored':
                        vertex_color[neighbor] = 'red' if vertex_color[current_vertex] == 'blue' else 'blue'
                        que.append(neighbor)
                    elif vertex_color[neighbor] == vertex_color[current_vertex]:
                        return False
    return True

# Example usage
if __name__ == "__main__":
    adj_list = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}
    print("Is the graph bipartite?", is_bipartite_graph(adj_list))
