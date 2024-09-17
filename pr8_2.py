from collections import deque

def bfs(graph, start_node):
    
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    result = []

    while queue:
        current_node = queue.popleft()
        result.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result 

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F'] 