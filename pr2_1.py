class Stack:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def _str_(self):
        return str(self.items)

def main():
    stack = Stack()
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Get size")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to push: ")
            stack.push(item)
            print(f"Stack after push: {stack}")
        elif choice == '2':
            try:
                popped_item = stack.pop()
                print(f"Popped item: {popped_item}")
                print(f"Stack after pop: {stack}")
            except IndexError as e:
                print(e)
        elif choice == '3':
            try:
                top_item = stack.peek()
                print(f"Top item: {top_item}")
            except IndexError as e:
                print(e)
        elif choice == '4':
            if stack.is_empty():
                print("Stack is empty")
            else:
                print("Stack is not empty")
        elif choice == '5':
            print(f"Stack size: {stack.size()}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()