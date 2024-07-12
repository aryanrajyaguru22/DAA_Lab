# Write A Python Code Finding factorial iterative approach

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")