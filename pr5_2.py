# Design an algorithm and implement a program for Binary Search and value entered by the user

def binarySearch(array, x):
    """
    Perform binary search on the array.
    
    Parameters:
    array (list): The input array.
    x (int): The target value to search for.
    
    Returns:
    int: The index of the target value if found, -1 otherwise.
    """
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    # Get the input array from the user
    array = input("Enter the array elements separated by space: ")
    array = [int(x) for x in array.split()]
    
    # Get the target value from the user
    x = int(input("Enter the target value to search for: "))
    
    # Perform binary search
    index = binarySearch(array, x)
    
    # Print the result
    if index != -1:
        print(f"Target value {x} found at index {index}")
    else:
        print(f"Target value {x} not found in the array")

if __name__ == "__main__":
    main()