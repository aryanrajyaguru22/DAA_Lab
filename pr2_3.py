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

class QueueUsingStacks:
    def _init_(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def front(self):
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def size(self):
        return self.stack1.size() + self.stack2.size()

    def _str_(self):
        return str(self.stack1.items[::-1] + self.stack2.items)

def main():
    queue = QueueUsingStacks()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Check if empty")
        print("5. Get size")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
            print(f"Queue after enqueue: {queue}")
        elif choice == '2':
            try:
                dequeued_item = queue.dequeue()
                print(f"Dequeued item: {dequeued_item}")
                print(f"Queue after dequeue: {queue}")
            except IndexError as e:
                print(e)
        elif choice == '3':
            try:
                front_item = queue.front()
                print(f"Front item: {front_item}")
            except IndexError as e:
                print(e)
        elif choice == '4':
            if queue.is_empty():
                print("Queue is empty")
            else:
                print("Queue is not empty")
        elif choice == '5':
            print(f"Queue size: {queue.size()}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()