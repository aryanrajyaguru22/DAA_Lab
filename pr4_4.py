# Design an algorithm and implement a program for Radix Sort
def counting_sort(arr, digit):

    size = len(arr)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = arr[i] // digit
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = arr[i] // digit
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

def radix_sort(arr):

    max_element = max(arr)
    digit = 1
    while max_element // digit > 0:
        counting_sort(arr, digit)
        digit *= 10

def get_user_input():

    num_elements = int(input("Enter the number of elements: "))
    arr = []
    for i in range(num_elements):
        num = int(input(f"Enter element {i+1}: "))
        arr.append(num)

    return arr

def main():
    arr = get_user_input()
    print("Original array:", arr)
    radix_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()