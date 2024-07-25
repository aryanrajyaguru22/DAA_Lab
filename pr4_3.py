# Design an algorithm and implement a program for Linear Search
def linear_search(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target value
    return -1  # Return -1 if the target value is not found

def get_user_input():
    num_elements = int(input("Enter the number of elements: "))
    arr = []
    for i in range(num_elements):
        num = int(input(f"Enter element {i+1}: "))
        arr.append(num)

    target = int(input("Enter the target value: "))

    return arr, target

def main():
    arr, target = get_user_input()
    result = linear_search(arr, target)

    if result != -1:
        print(f"Target value {target} found at index {result}.")
    else:
        print(f"Target value {target} not found in the list.")

if __name__ == "__main__":
    main()