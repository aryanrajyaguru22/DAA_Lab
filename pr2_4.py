from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(list(self.items))

class StackUsingQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def is_empty(self):
        return self.queue1.is_empty()

    def push(self, item):
        self.queue2.enqueue(item)
        while not self.queue1.is_empty():
            self.queue2.enqueue(self.queue1.dequeue())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.queue1.dequeue()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.queue1.front()

    def size(self):
        return self.queue1.size()

    def __str__(self):
        return str(self.queue1)

def main():
    stack = StackUsingQueues()
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

if __name__ == "__main__":
    main()
