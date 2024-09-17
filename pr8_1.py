def dfs(graph, start_node):
    
    visited = set()  # Set to keep track of visited nodes
    visited_nodes = []

    def dfs_helper(node):
        visited.add(node)
        visited_nodes.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)
    
    dfs_helper(start_node)
    return visited_nodes

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(dfs(graph, 'A'))  # Output: ['A', 'B', 'D', 'E', 'F', 'C']