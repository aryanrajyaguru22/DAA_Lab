# Design an algorithm and implement a program for Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Get input from the user
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    arr.append(elem)

print("Original array:", arr)

# Sort the array using Insertion Sort
insertion_sort(arr)

print("Sorted array:", arr)
