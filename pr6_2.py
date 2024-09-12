# Design an algorithm and implement a program to solve the Knapsack Problem value enter by user(Greedy Approach)
def knapsack_greedy():
    num_items = int(input("Enter the number of items: "))
    capacity = int(input("Enter the knapsack's capacity: "))
    items = []
    for i in range(num_items):
        weight = int(input(f"Enter weight of item {i+1}: "))
        value = int(input(f"Enter value of item {i+1}: "))
        items.append((weight, value))

    ratios = [(value / weight, weight, value) for weight, value in items]

    ratios.sort(reverse=True)

    total_value = 0
    total_weight = 0
    included_items = []

    for ratio, weight, value in ratios:
        if total_weight + weight <= capacity:
            total_value += value
            total_weight += weight
            included_items.append((weight, value))
        else:
            break

    print("Total value:", total_value)
    print("Included items:", included_items)

knapsack_greedy()