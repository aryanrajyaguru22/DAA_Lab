# Design an algorithm and implement a program to solve Finding Optimal Matrix Chain Order Problem and Value Enter by User (Dynamic Programming approach)

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        m[i][i] = 0

    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

n = int(input("Enter the number of matrices: "))
p = [0] * (n + 1)
for i in range(n + 1):
    p[i] = int(input(f"Enter the number of rows in matrix {i} (and number of columns in matrix {i - 1}): "))

m, s = matrix_chain_order(p)

print("Optimal parenthesization: ", end="")
print_optimal_parens(s, 1, n)
print("\nMinimum number of scalar multiplications: " + str(m[1][n]))