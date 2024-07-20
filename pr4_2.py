# Design an algorithm and implement a program for Selection
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Get input from the user
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    arr.append(elem)

print("Original array:", arr)

# Sort the array using Selection Sort
selection_sort(arr)

print("Sorted array:", arr)
