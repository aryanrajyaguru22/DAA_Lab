# Design an algorithm and write a program to implement Breadth First Search of a graph values enter by the user(Graph Algorithms)

from collections import deque

def bfs(graph, start):
    visited = set()
    traversal_order = []
    queue = deque()

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        traversal_order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return traversal_order


# Get graph values from user
num_nodes = int(input("Enter the number of nodes: "))
graph = {}

for i in range(num_nodes):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start_node = input("Enter the start node: ")

# Perform BFS
traversal_order = bfs(graph, start_node)

print("Breadth-First Search Traversal Order:", traversal_order)