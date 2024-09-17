# Design an algorithm and implement a program for The Assignment Problem in Branch and Bound

import sys

def branch_and_bound(cost_matrix):
    n = len(cost_matrix)
    min_cost = sys.maxsize
    min_assignment = None

    def recursive_branch_and_bound(i, current_cost, current_assignment, rows, cols):
        nonlocal min_cost, min_assignment

        if i == n:
            if current_cost < min_cost:
                min_cost = current_cost
                min_assignment = current_assignment[:]
            return

        min_val = sys.maxsize
        for j in range(n):
            if cols[j] == 0:
                min_val = min(min_val, cost_matrix[i][j])

        for j in range(n):
            if cols[j] == 0:
                rows[i] = 1
                cols[j] = 1
                recursive_branch_and_bound(i + 1, current_cost + cost_matrix[i][j] - min_val, current_assignment + [(i, j)], rows, cols)
                rows[i] = 0
                cols[j] = 0

    def reduce_matrix(matrix):
        n = len(matrix)
        min_row = [sys.maxsize] * n
        min_col = [sys.maxsize] * n

        for i in range(n):
            for j in range(n):
                min_row[i] = min(min_row[i], matrix[i][j])
                min_col[j] = min(min_col[j], matrix[i][j])

        for i in range(n):
            for j in range(n):
                matrix[i][j] -= min_row[i] + min_col[j]

        return matrix

    reduced_matrix = reduce_matrix(cost_matrix)
    rows = [0] * n
    cols = [0] * n
    recursive_branch_and_bound(0, 0, [], rows, cols)

    return min_cost, min_assignment


# Get the number of tasks and agents from the user
n = int(input("Enter the number of tasks and agents: "))

# Create an empty cost matrix
cost_matrix = []

# Get the cost matrix from the user
for _ in range(n):
    row = list(map(int, input("Enter the costs for an agent: ").split()))
    cost_matrix.append(row)

# Solve the assignment problem using Branch and Bound
min_cost, min_assignment = branch_and_bound(cost_matrix)

# Print the minimum cost and assignment
print("Minimum Cost:", min_cost)
print("Assignment:")
for i, (task, agent) in enumerate(min_assignment):
    print(f"Task {i + 1} -> Agent {agent + 1}")