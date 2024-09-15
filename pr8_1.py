# Design an algorithm and write a program to implement Depth First Search of a graph values enter by user(Graph Algorithms)

def dfs(graph, start):
    visited = set()
    traversal_order = []

    def dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return traversal_order


# Get graph values from user
num_nodes = int(input("Enter the number of nodes: "))
graph = {}

for i in range(num_nodes):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter the start node: ")

# Perform DFS
traversal_order = dfs(graph, start_node)

print("Depth-First Search Traversal Order:", traversal_order)