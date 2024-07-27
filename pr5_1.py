# Design an algorithm and implement a program for Quick Sort and value enter by user

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def main():
    array = input("Enter the array elements separated by space: ")
    array = [int(x) for x in array.split()]
    
    quickSort(array, 0, len(array) - 1)
    print("Sorted Array:")
    print(array)

if __name__ == "__main__":
    main()